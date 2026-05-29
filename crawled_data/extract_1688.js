(() => {
  const items = Array.from(document.querySelectorAll('a[href*="offer/"], a[href*="ci_bb"], a[href*="ci_king"]'));
  const results = [];
  const category = '常规热销日百';
  
  items.forEach(item => {
    const titleEl = item.querySelector('.title, .name, [class*="title"], [class*="name"]');
    const priceEl = item.querySelector('.price, [class*="price"]');
    const imgEl = item.querySelector('img');
    
    // Some items might not have title or price in the expected classes
    // Let's try to find them by text or other means if null
    let title = titleEl ? titleEl.innerText.trim() : '';
    if (!title) {
        // Fallback to searching all text for something that looks like a title
        title = item.innerText.split('\n')[0].trim();
    }
    
    let priceText = priceEl ? priceEl.innerText.trim() : '';
    if (!priceText) {
        const priceMatch = item.innerText.match(/￥\s*(\d+\.?\d*)/);
        if (priceMatch) priceText = priceMatch[1];
    } else {
        priceText = priceText.replace('￥', '').trim();
    }
    
    let moq = '1'; // Default
    const moqMatch = item.innerText.match(/(\d+)件起\s*批/);
    if (moqMatch) moq = moqMatch[1];
    
    const imgUrl = imgEl ? imgEl.src : '';
    
    if (title && priceText && imgUrl) {
      results.push({
        category,
        title,
        price: priceText,
        MOQ: moq,
        imageUrl: imgUrl
      });
    }
  });
  
  // Deduplicate by title
  const uniqueResults = [];
  const titles = new Set();
  results.forEach(r => {
    if (!titles.has(r.title)) {
      titles.add(r.title);
      uniqueResults.push(r);
    }
  });
  
  return uniqueResults;
})()