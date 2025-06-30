document.querySelectorAll('.container-carousel').forEach((container) => {
  const carousel = container.querySelector('.carousel');
  const btnLeft = container.querySelector('.voltar');
  const btnRight = container.querySelector('.avancar');

  // Pega a largura do primeiro card e inclui a margem (gap)
  const cardWidth = container.querySelector('.cardmidia').offsetWidth + 550;

  // Clona os elementos para criar um loop infinito
  const cards = Array.from(carousel.children);
  cards.forEach((card) => {
    const clone = card.cloneNode(true);
    carousel.appendChild(clone);
  });

  // Número total de cards (incluindo os duplicados)
  const totalCards = carousel.children.length;
  let scrollPosition = 0;

  function moveLeft() {
    if (scrollPosition >= 0) {
      // Se estiver no primeiro, volta para o fim instantaneamente
      scrollPosition = -(cardWidth * (totalCards / 2));
      carousel.style.transition = 'none';
      carousel.style.transform = `translateX(${scrollPosition}px)`;
      setTimeout(() => {
        carousel.style.transition = 'transform 0.5s ease-in-out';
        scrollPosition += cardWidth;
        carousel.style.transform = `translateX(${scrollPosition}px)`;
      }, 10);
    } else {
      scrollPosition += cardWidth;
      carousel.style.transition = 'transform 0.5s ease-in-out';
      carousel.style.transform = `translateX(${scrollPosition}px)`;
    }
  }

  function moveRight() {
    if (scrollPosition <= -(cardWidth * (totalCards / 2))) {
      // Se estiver no último, volta para o primeiro instantaneamente
      scrollPosition = 0;
      carousel.style.transition = 'none';
      carousel.style.transform = `translateX(${scrollPosition}px)`;
      setTimeout(() => {
        carousel.style.transition = 'transform 0.5s ease-in-out';
        scrollPosition -= cardWidth;
        carousel.style.transform = `translateX(${scrollPosition}px)`;
      }, 10);
    } else {
      scrollPosition -= cardWidth;
      carousel.style.transition = 'transform 0.5s ease-in-out';
      carousel.style.transform = `translateX(${scrollPosition}px)`;
    }
  }

  // Adiciona os eventos aos botões
  btnLeft.addEventListener('click', moveLeft);
  btnRight.addEventListener('click', moveRight);
});
