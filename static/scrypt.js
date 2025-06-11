document.addEventListener('DOMContentLoaded', function() {
    const wrapper = document.querySelector('.carousel-wrapper');
    if (!wrapper) return; // Если нет карусели, выходим
    
    const carousel = wrapper.querySelector('.carousel');
    const leftBtn = wrapper.querySelector('.carousel-btn.left');
    const rightBtn = wrapper.querySelector('.carousel-btn.right');

    // Проверяем, что элементы существуют
    if (!carousel || !leftBtn || !rightBtn) {
        console.error('Не найдены элементы карусели!');
        return;
    }

    // Шаг прокрутки = ширина карточки + отступ
    const scrollStep = 320; // 300px (карточка) + 20px (gap)

    leftBtn.addEventListener('click', () => {
        carousel.scrollBy({ left: -scrollStep, behavior: 'smooth' });
    });

    rightBtn.addEventListener('click', () => {
        carousel.scrollBy({ left: scrollStep, behavior: 'smooth' });
    });

    console.log('Карусель инициализирована!'); // Проверка в консоли
});

function show_files_name(input) {
    const output = input.nextElementSibling;
    if (!output) return;
    output.innerHTML = '';

    if (input.files.length > 0) {
        const ul = document.createElement('ul');
        for (let i = 0; i < input.files.length; i++) {
            const li = document.createElement('li');
            li.textContent = input.files[i].name;
            ul.appendChild(li);
        }
        output.appendChild(ul);
    }
}
