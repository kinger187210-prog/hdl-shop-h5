(() => {
  const items = Array.from(document.querySelectorAll('.search-offer-wrapper'));
  return items.map(item => {
    let title = "";
    const titleEl = item.querySelector('.title, .offer-title, [class*="title"]');
    if (titleEl) title = titleEl.innerText.trim();
    if (!title) {
        const img = item.querySelector('img');
        if (img) title = img.alt || img.title;
    }
    if (!title) {
        title = item.innerText.split('\n')[0].trim();
    }

    let price = "";
    const priceEl = item.querySelector('.price, [class*="price"]');
    if (priceEl) {
        price = priceEl.innerText.replace(/\n/g, '').trim();
    }
    if (!price || !price.includes('¥')) {
        const match = item.innerText.match(/¥\s*([\d\.]+)/);
        if (match) price = match[0];
    }
    const priceMatch = price.match(/¥[\d\.]+/);
    price = priceMatch ? priceMatch[0] : "";

    let moq = "1";
    const moqMatch = item.innerText.match(/(\d+)件起批/);
    if (moqMatch) moq = moqMatch[1];

    const imgEl = item.querySelector('img');
    let imageUrl = imgEl ? (imgEl.getAttribute('src') || imgEl.getAttribute('data-src') || imgEl.getAttribute('original-src')) : "";
    if (imageUrl && imageUrl.startsWith('//')) imageUrl = 'https:' + imageUrl;

    return {
      category: '五金工具与家居维修',
      title,
      price,
      moq,
      imageUrl
    };
  }).filter(item => item.title && item.price && item.imageUrl);
})()