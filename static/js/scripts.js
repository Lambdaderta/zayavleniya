document.addEventListener('DOMContentLoaded', () => {
    const dropdownButton = document.getElementById('dropdown-button');
    const dropdownMenu = document.getElementById('dropdown-menu');
    const themeToggleButton = document.getElementById('theme-toggle-button');
    const backButton = document.getElementById('back-button');
    const actionButtons = document.querySelectorAll('.action-button');

    dropdownButton.addEventListener('click', () => {
        dropdownMenu.classList.toggle('hidden');
    });

    themeToggleButton.addEventListener('click', () => {
        document.body.classList.toggle('light-theme');
        document.body.classList.toggle('dark-theme');
    });

    actionButtons.forEach(button => {
        button.addEventListener('click', () => {
            actionButtons.forEach(btn => btn.classList.add('hidden'));
            backButton.classList.remove('hidden');
        });
    });

    backButton.addEventListener('click', () => {
        actionButtons.forEach(btn => btn.classList.remove('hidden'));
        backButton.classList.add('hidden');
    });
});