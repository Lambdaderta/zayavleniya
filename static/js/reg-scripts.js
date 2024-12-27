document.addEventListener('DOMContentLoaded', () => {
    const parentButton = document.getElementById('parent-button');
    const teacherButton = document.getElementById('teacher-button');
    const accountTypeField = document.getElementById('account-type');
    const registrationForm = document.getElementById('registration-form');
    const teacherFields = document.getElementById('teacher-fields'); 
    const commonFields = document.getElementById('common-fields'); 
    const sbm = document.getElementById('sbm');

    parentButton.addEventListener('click', () => {
        teacherFields.classList.add('hidden');
        sbm.classList.remove('hidden'); 
        commonFields.classList.remove('hidden'); 
        accountTypeField.value = 'parent'; 
        registrationForm.classList.remove('hidden');
    });

    teacherButton.addEventListener('click', () => {
        teacherFields.classList.remove('hidden');
        accountTypeField.value = 'teacher';
        commonFields.classList.remove('hidden'); 
        sbm.classList.remove('hidden'); 
        registrationForm.classList.remove('hidden'); 
    });
});