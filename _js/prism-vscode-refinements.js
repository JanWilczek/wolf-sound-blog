// Build-time Prism refinements that bring token classification closer to
// VS Code's TextMate grammars, so that prism-vscode-dark-modern.css can
// reproduce the Dark Modern theme. Keyword lists are taken from the grammars
// bundled with VS Code (cpp, MagicPython, rust, java, shellscript) and the
// fwcd.kotlin extension.
const loadLanguages = require("prismjs/components/index.js");

const LANGUAGE_ALIASES = {
  "c++": "cpp",
  py: "python",
  rs: "rust",
  kt: "kotlin",
  kts: "kotlin",
  sh: "bash",
  shell: "bash",
  js: "javascript",
  ts: "typescript",
};

// Keywords scoped as `keyword.control.*` (and a few others coloured the same
// way by Dark+, e.g. C++ `using`, `operator`, `new`, `delete`).
const CPP_CONTROL_FLOW = [
  "break", "case", "catch", "continue", "default", "do", "else", "for",
  "goto", "if", "return", "switch", "throw", "try", "while",
];
const JS_CONTROL_FLOW = [
  ...CPP_CONTROL_FLOW, "as", "await", "export", "finally", "from", "import",
  "yield",
];

const CONTROL_FLOW_KEYWORDS = {
  c: new Set(CPP_CONTROL_FLOW),
  cpp: new Set([
    ...CPP_CONTROL_FLOW, "co_await", "co_return", "co_yield", "delete",
    "import", "new", "operator", "using",
  ]),
  python: new Set([
    "as", "assert", "async", "await", "break", "case", "continue", "del",
    "elif", "else", "except", "finally", "for", "from", "if", "import",
    "match", "pass", "raise", "return", "try", "while", "with", "yield",
  ]),
  rust: new Set([
    "await", "break", "continue", "do", "else", "for", "if", "loop", "match",
    "return", "try", "while", "yield",
  ]),
  kotlin: new Set([
    "break", "continue", "do", "else", "for", "if", "return", "throw", "try",
    "when", "while",
  ]),
  java: new Set([
    ...CPP_CONTROL_FLOW, "finally", "new", "yield",
  ]),
  javascript: new Set(JS_CONTROL_FLOW),
  typescript: new Set(JS_CONTROL_FLOW),
  bash: new Set([
    "case", "continue", "do", "done", "elif", "else", "esac", "fi", "for",
    "if", "in", "return", "select", "then", "until", "while",
  ]),
};

// Python builtins scoped as `support.type.python` (teal) rather than
// `support.function.builtin.python` (yellow).
const PYTHON_BUILTIN_TYPES = new Set([
  "bool", "bytearray", "bytes", "classmethod", "complex", "dict", "float",
  "frozenset", "int", "list", "memoryview", "object", "property", "set",
  "slice", "staticmethod", "str", "tuple", "type",
]);

const OPENING_BRACKETS = new Set(["(", "[", "{"]);
const CLOSING_BRACKETS = new Set([")", "]", "}"]);
// VS Code cycles through editorBracketHighlight.foreground1..3 by default.
const BRACKET_COLOR_COUNT = 3;

const addAlias = (token, alias) => {
  const aliases = Array.isArray(token.alias)
    ? token.alias
    : token.alias ? [token.alias] : [];
  token.alias = [...aliases, alias];
};

const forEachToken = (tokens, callback) => {
  for (const token of tokens) {
    if (typeof token === "string") {
      continue;
    }
    callback(token);
    if (Array.isArray(token.content)) {
      forEachToken(token.content, callback);
    }
  }
};

const isBracket = (token, brackets) =>
  token.type === "punctuation" &&
  typeof token.content === "string" &&
  brackets.has(token.content);

// Splits keywords into control flow (purple) and declarations (blue), and
// reclassifies keywords that VS Code scopes as types.
const refineKeywords = (tokens, language) => {
  const controlFlow = CONTROL_FLOW_KEYWORDS[language];
  forEachToken(tokens, (token) => {
    if (typeof token.content !== "string") {
      return;
    }
    if (token.type === "keyword") {
      if (/^\w+_t$/.test(token.content)) {
        // e.g. uint32_t: support.type.posix-reserved
        token.type = "class-name";
      } else if (controlFlow?.has(token.content)) {
        addAlias(token, "control-flow");
      }
    } else if (
      token.type === "builtin" &&
      language === "python" &&
      PYTHON_BUILTIN_TYPES.has(token.content)
    ) {
      token.type = "class-name";
    }
  });
};

// Python f-string braces are part of the string scope in VS Code, so they are
// coloured as placeholders and excluded from bracket pair colorization.
const markInterpolationBraces = (tokens) => {
  forEachToken(tokens, (token) => {
    if (token.type !== "interpolation" || !Array.isArray(token.content)) {
      return;
    }
    const first = token.content[0];
    const last = token.content[token.content.length - 1];
    if (typeof first !== "string" && isBracket(first, OPENING_BRACKETS)) {
      first.type = "interpolation-punctuation";
      addAlias(first, "punctuation");
    }
    if (typeof last !== "string" && isBracket(last, CLOSING_BRACKETS)) {
      last.type = "interpolation-punctuation";
      addAlias(last, "punctuation");
    }
  });
};

// Emulates VS Code's bracket pair colorization: each bracket gets a
// `brace-level-N` alias based on its nesting depth.
const colorizeBracketPairs = (tokens) => {
  let depth = 0;
  forEachToken(tokens, (token) => {
    if (isBracket(token, OPENING_BRACKETS)) {
      addAlias(token, `brace-level-${(depth % BRACKET_COLOR_COUNT) + 1}`);
      depth += 1;
    } else if (isBracket(token, CLOSING_BRACKETS)) {
      depth = Math.max(depth - 1, 0);
      addAlias(token, `brace-level-${(depth % BRACKET_COLOR_COUNT) + 1}`);
    }
  });
};

/**
 * Registers the VS Code refinements on the given Prism instance.
 * Intended for the `init` option of @11ty/eleventy-plugin-syntaxhighlight.
 */
const applyVsCodeRefinements = (Prism) => {
  loadLanguages(["cpp", "python"]);

  // `std` in `std::vector`: entity.name.scope-resolution
  Prism.languages.insertBefore("cpp", "keyword", {
    "scope-resolution": {
      pattern: /\b[A-Za-z_]\w*(?=\s*::)/,
      alias: "class-name",
    },
  });

  // Python only tokenises function definitions; VS Code also colours calls.
  // Inserted after `keyword` and `builtin` so those keep precedence.
  Prism.languages.insertBefore("python", "boolean", {
    "function-call": {
      pattern: /\b[A-Za-z_]\w*(?=\s*\()/,
      alias: "function",
    },
  });

  Prism.hooks.add("after-tokenize", (env) => {
    const language = LANGUAGE_ALIASES[env.language] ?? env.language;
    refineKeywords(env.tokens, language);
    markInterpolationBraces(env.tokens);
    colorizeBracketPairs(env.tokens);
  });
};

module.exports = { applyVsCodeRefinements };
