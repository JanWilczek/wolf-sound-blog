// Early theme detection to prevent flash of wrong theme
(() => {
    const getStoredTheme = () => localStorage.getItem('theme');
    const setStoredTheme = theme => localStorage.setItem('theme', theme);

    const setTheme = theme => {
        document.documentElement.setAttribute('data-bs-theme', theme);

        // Upon first open, user system theme is saved
        setStoredTheme(theme);
    }

    const getPreferredTheme = () => {
        const stored = getStoredTheme();
        if (stored) {
            return stored;
        }

        const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
        return prefersDark ? 'dark' : 'light';
    };

    setTheme(getPreferredTheme());

    window.addEventListener('DOMContentLoaded', () => {
        const showActiveTheme = theme => {
            const sunIcon = document.getElementById('themeIconSun');
            const moonIcon = document.getElementById('themeIconMoon');
            if (sunIcon && moonIcon) {
                // Show sun in dark mode (to switch to light), moon in light mode (to switch to dark)
                sunIcon.style.display = theme === 'dark' ? 'inline-block' : 'none';
                moonIcon.style.display = theme === 'light' ? 'inline-block' : 'none';
            }
        };

        const updatePrismTheme = theme => {
            const prismLink = document.getElementById('prism-theme');
            if (prismLink) {
                prismLink.href = theme === 'dark'
                    ? '/assets/css/prism-tomorrow-night.css'
                    : '/assets/css/prism-coy.css';
            }
        };

        const currentTheme = getPreferredTheme();
        showActiveTheme(currentTheme);
        updatePrismTheme(currentTheme);

        const toggleTheme = () => {
            const current = document.documentElement.getAttribute('data-bs-theme');
            const newTheme = current === 'dark' ? 'light' : 'dark';
            setTheme(newTheme);
            showActiveTheme(newTheme);
            updatePrismTheme(newTheme);
        }

        const toggleBtn = document.getElementById('themeToggle');
        if (toggleBtn) {
            toggleBtn.addEventListener('click', toggleTheme);
        }
    });
})();
