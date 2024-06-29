document.addEventListener('DOMContentLoaded', function() {
    const categoryField = document.querySelector('#id_category');
    const subcategoryField = document.querySelector('#id_subcategory');
    const originalSubcategoryOptions = Array.from(subcategoryField.options);

    categoryField.addEventListener('change', function() {
        const categoryId = this.value;
        subcategoryField.innerHTML = '';
        const filteredOptions = originalSubcategoryOptions.filter(option => option.dataset.categoryId === categoryId);
        filteredOptions.forEach(option => subcategoryField.add(option));
    });

    categoryField.dispatchEvent(new Event('change'));
});