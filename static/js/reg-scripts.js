document.addEventListener('DOMContentLoaded', () => {
    const parentButton = document.getElementById('parent-button');
    const teacherButton = document.getElementById('teacher-button');
    const accountTypeField = document.getElementById('account-type');
    const registrationForm = document.getElementById('registration-form');
    const teacherFields = document.getElementById('teacher-fields');

    parentButton.addEventListener('click', () => {
        teacherFields.classList.add('hidden'); 
        accountTypeField.value = 'parent'; 
        registrationForm.classList.remove('hidden');
    });

    teacherButton.addEventListener('click', () => {
        teacherFields.classList.remove('hidden');
        accountTypeField.value = 'teacher'; 
        registrationForm.classList.remove('hidden'); 
    });
});