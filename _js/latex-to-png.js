// Node.js script to convert LaTeX equations to PNG files without background
const fs = require('fs');
const path = require('path');
const { exec } = require('child_process');
const util = require('util');
const execPromise = util.promisify(exec);

// Configuration
const inputFile = 'equations.txt'; // Change this to your input file
const outputDir = 'equations';
const tempDir = 'temp_latex';

// Create output and temp directories if they don't exist
if (!fs.existsSync(outputDir)) {
  fs.mkdirSync(outputDir);
}
if (!fs.existsSync(tempDir)) {
  fs.mkdirSync(tempDir);
}

// LaTeX template with transparent background
const latexTemplate = `
\\documentclass[preview,border=0.5pt]{standalone}
\\usepackage{amsmath}
\\usepackage{amssymb}
\\usepackage{amsfonts}
\\usepackage{color}
\\usepackage{transparent}
\\begin{document}
%EQUATION%
\\end{document}
`;

// Read the equations file
async function processEquations() {
  try {
    const data = fs.readFileSync(inputFile, 'utf8');
    const equations = data.split('\n\n').filter(eq => eq.trim() !== '');
    
    console.log(`Found ${equations.length} equations to process`);
    
    for (let i = 0; i < equations.length; i++) {
      const equation = equations[i].trim();
      console.log(`Processing equation ${i+1}/${equations.length}`);
      await processEquation(equation, i+1);
    }
    
    console.log('All equations have been processed');
    console.log(`PNG files are saved in the '${outputDir}' directory`);
    
    // Clean up temp directory
    fs.rmSync(tempDir, { recursive: true, force: true });
  } catch (err) {
    console.error('Error processing equations:', err);
  }
}

// Process a single equation
async function processEquation(equation, index) {
  const texFilename = path.join(tempDir, `equation_${index}.tex`);
  const pdfFilename = path.join(tempDir, `equation_${index}.pdf`);
  const pngFilename = path.join(outputDir, `equation_${index}.png`);
  
  // Replace the placeholder with the actual equation
  const texContent = latexTemplate.replace('%EQUATION%', equation);
  
  // Write the tex file
  fs.writeFileSync(texFilename, texContent);
  
  try {
    // Compile LaTeX to PDF
    await execPromise(`pdflatex -interaction=nonstopmode -output-directory=${tempDir} ${texFilename}`);
    
    // Convert PDF to PNG with transparent background
    await execPromise(`convert -density 300 ${pdfFilename} -quality 100 -transparent white ${pngFilename}`);
    
    console.log(`Successfully rendered equation ${index} to ${pngFilename}`);
  } catch (error) {
    console.error(`Error processing equation ${index}:`, error.message);
  }
}

// Run the script
processEquations();
