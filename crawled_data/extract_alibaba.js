
(async () => {
    const products = [];
    const items = document.querySelectorAll('.search-card-e, .list-no-v2-main-card, [data-content="productItem"]');
    
    items.forEach(item => {
        try {
            const titleEl = item.querySelector('h2, .search-card-e-title, .elements-title-normal');
            const priceEl = item.querySelector('.search-card-e-price-main, .elements-offer-price-normal');
            const moqEl = item.querySelector('.search-card-e-min-order, .element-offer-minorder-normal');
            const imgEl = item.querySelector('img.search-card-e-photo, img.elements-img-ratio-can, .search-card-e-slider-image img');

            if (titleEl && priceEl) {
                products.push({
                    title: titleEl.innerText.trim(),
                    price: priceEl.innerText.trim(),
                    moq: moqEl ? moqEl.innerText.trim() : 'N/A',
                    image: imgEl ? imgEl.src : 'N/A',
                    category: '性价比高的电子产品周边'
                });
            }
        } catch (e) {}
    });
    
    return products;
})();
