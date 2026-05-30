(function() {
    // --- State ---
    let allProducts = [];
    let filteredProducts = [];
    let cart = new Map(); // id -> {product, count}
    let currentView = 'home';
    let pagination = {
        home: { offset: 0, limit: 20 },
        category: { offset: 0, limit: 20 },
        search: { offset: 0, limit: 20 }
    };
    let categories = [];
    let activeCategory = null;

    // --- DOM Elements ---
    const app = document.getElementById('app');
    const views = document.querySelectorAll('.view');
    const tabBtns = document.querySelectorAll('.tab-btn');
    const globalSearchInput = document.getElementById('global-search');
    const searchBtn = document.getElementById('search-btn');
    const cartBadge = document.getElementById('cart-badge');
    const tplProduct = document.getElementById('tpl-product');

    const targetCategories = ["冬季保暖", "电子周边", "五金工具", "车载用品", "日百", "户外露营", "家居装饰", "厨房厨具", "母婴玩具", "宠物用品"];

    // --- Initialization ---
    async function init() {
        showLoading();
        try {
            const response = await fetch('hdl_inventory.json?v=' + Date.now());
            allProducts = await response.json();
            console.log('Loaded products:', allProducts.length);
            
            // Extract categories (using 'category' field)
            const catMap = new Set();
            allProducts.forEach(p => {
                if (p.category) catMap.add(p.category);
                else if (p.material) catMap.add(p.material);
                else if (p.brand) catMap.add(p.brand);
            });
            
            // Merge target categories and other existing categories
            const existingCats = Array.from(catMap);
            const otherCats = existingCats.filter(c => c && !targetCategories.includes(c));
            categories = ['全部', ...targetCategories, ...otherCats.filter(c => c.length < 15).slice(0, 15)];
            
            setupEventListeners();
            renderCategories();
            handleRouting();
            updateCartBadge();
        } catch (err) {
            console.error('Failed to load data:', err);
            alert('加载数据失败，请确保 hdl_inventory.json 在同一目录下。');
        } finally {
            hideLoading();
        }
    }

    // --- Routing ---
    function handleRouting() {
        const hash = window.location.hash.replace('#', '') || 'home';
        const [view, id] = hash.split('/');
        
        if (view === 'detail' && id) {
            showDetail(id);
        } else {
            switchView(view);
        }
    }

    function switchView(viewName) {
        currentView = viewName;
        views.forEach(v => v.classList.add('hidden'));
        const activeView = document.getElementById(`view-${viewName}`);
        if (activeView) activeView.classList.remove('hidden');

        // Update Tab Bar
        tabBtns.forEach(btn => {
            const isTarget = btn.dataset.target === viewName;
            btn.classList.toggle('text-blue-600', isTarget);
            btn.classList.toggle('text-gray-500', !isTarget);
            btn.classList.toggle('tab-active', isTarget);
        });

        // Specific View Actions
        if (viewName === 'home') {
            renderHome();
        } else if (viewName === 'category') {
            renderCategoryProducts();
        } else if (viewName === 'cart') {
            renderCart();
        }
        
        window.scrollTo(0, 0);
    }

    // --- Rendering ---
    function renderProductCard(product) {
        const clone = tplProduct.content.cloneNode(true);
        const card = clone.querySelector('.product-card');
        const img = clone.querySelector('img');
        const name = clone.querySelector('.product-name');
        const model = clone.querySelector('.product-model');
        const price = clone.querySelector('.product-price');
        const btn = clone.querySelector('.add-to-cart-btn');

        card.dataset.id = product.id;
        img.src = product.sPicUrl || 'https://via.placeholder.com/150?text=No+Image';
        img.setAttribute('referrerpolicy', 'no-referrer');
        name.textContent = product.ProductName;
        model.textContent = `货号: ${product.ProModel}`;
        price.textContent = product.price_display;

        card.addEventListener('click', (e) => {
            if (e.target.closest('.add-to-cart-btn')) return;
            window.location.hash = `detail/${product.id}`;
        });

        btn.addEventListener('click', (e) => {
            e.stopPropagation();
            addToCart(product);
            animateButton(btn);
        });

        return clone;
    }

    function renderHome() {
        const container = document.getElementById('category-selection-module');
        container.innerHTML = '';
        
        targetCategories.forEach(cat => {
            const catProducts = allProducts.filter(p => p.category === cat);
            if (catProducts.length === 0) return;

            // Pick 3-5 random products
            const count = Math.min(catProducts.length, Math.floor(Math.random() * 3) + 3);
            const shuffled = [...catProducts].sort(() => 0.5 - Math.random());
            const selection = shuffled.slice(0, count);

            const section = document.createElement('div');
            section.className = 'category-section bg-white rounded-lg p-3 shadow-sm';
            section.innerHTML = `
                <div class="flex justify-between items-center mb-3">
                    <h2 class="text-lg font-bold text-gray-800 border-l-4 border-blue-600 pl-2">${cat}</h2>
                    <button class="text-sm text-blue-600 font-medium more-btn" data-category="${cat}">更多 ></button>
                </div>
                <div class="grid grid-cols-2 gap-3 product-grid">
                </div>
            `;

            const grid = section.querySelector('.product-grid');
            selection.forEach(p => {
                grid.appendChild(renderProductCard(p));
            });

            section.querySelector('.more-btn').onclick = () => {
                activeCategory = cat;
                window.location.hash = 'category';
                // Trigger re-render of category view
                renderCategories();
                pagination.category.offset = 0;
                renderCategoryProducts(true);
            };

            container.appendChild(section);
        });
    }

    function renderCategories() {
        const list = document.getElementById('category-list');
        list.innerHTML = '';
        categories.forEach(cat => {
            const div = document.createElement('div');
            div.className = 'p-4 text-sm border-b cursor-pointer transition-colors hover:bg-gray-50';
            div.textContent = cat;
            if (activeCategory === cat || (!activeCategory && cat === '全部')) {
                div.classList.add('category-active');
            }
            div.onclick = () => {
                activeCategory = cat === '全部' ? null : cat;
                document.querySelectorAll('#category-list div').forEach(d => d.classList.remove('category-active'));
                div.classList.add('category-active');
                pagination.category.offset = 0;
                renderCategoryProducts(true);
            };
            list.appendChild(div);
        });
    }

    function renderCategoryProducts(reset = false) {
        const container = document.getElementById('category-products');
        if (reset) container.innerHTML = '';
        
        const filtered = activeCategory 
            ? allProducts.filter(p => p.category === activeCategory)
            : allProducts;
        
        const { offset, limit } = pagination.category;
        const chunk = filtered.slice(offset, offset + limit);
        
        chunk.forEach(p => container.appendChild(renderProductCard(p)));
        pagination.category.offset += limit;
    }

    function renderSearchResults(reset = false) {
        const container = document.getElementById('search-results');
        const countLabel = document.getElementById('search-count');
        if (reset) {
            container.innerHTML = '';
            pagination.search.offset = 0;
            const query = globalSearchInput.value.trim().toLowerCase();
            if (!query) {
                filteredProducts = [];
            } else {
                filteredProducts = allProducts.filter(p => 
                    p.ProductName.toLowerCase().includes(query) || 
                    p.ProModel.toLowerCase().includes(query)
                );
            }
            countLabel.textContent = `找到 ${filteredProducts.length} 个商品`;
        }
        
        const { offset, limit } = pagination.search;
        const chunk = filteredProducts.slice(offset, offset + limit);
        
        chunk.forEach(p => container.appendChild(renderProductCard(p)));
        pagination.search.offset += limit;
    }

    function showDetail(id) {
        const product = allProducts.find(p => p.id === id);
        if (!product) return;

        currentView = 'detail';
        views.forEach(v => v.classList.add('hidden'));
        const detailView = document.getElementById('view-detail');
        detailView.classList.remove('hidden');

        const content = document.getElementById('detail-content');
        content.innerHTML = `
            <div class="relative">
                <button onclick="history.back()" class="absolute top-4 left-4 bg-black bg-opacity-30 text-white p-2 rounded-full z-10">
                    <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7"></path></svg>
                </button>
                <img src="${product.sPicUrl || 'https://via.placeholder.com/400'}" referrerpolicy="no-referrer" class="w-full aspect-square object-cover">
            </div>
            <div class="p-4">
                <div class="flex justify-between items-start mb-2">
                    <h1 class="text-xl font-bold text-gray-900">${product.ProductName}</h1>
                    <span class="text-red-500 font-bold text-lg">${product.price_display}</span>
                </div>
                <p class="text-gray-500 text-sm mb-4">货号: ${product.ProModel}</p>
                
                <div class="bg-gray-50 rounded-lg p-3 space-y-2 text-sm">
                    <div class="flex justify-between"><span class="text-gray-400">规格:</span><span>${product.Specifications || '见详情'}</span></div>
                    <div class="flex justify-between"><span class="text-gray-400">材质:</span><span>${product.material || '默认'}</span></div>
                    <div class="flex justify-between"><span class="text-gray-400">装箱数:</span><span>${product.Packing_number || '-'}</span></div>
                    <div class="flex justify-between"><span class="text-gray-400">体积:</span><span>${product.zxvolume || '-'}</span></div>
                    <div class="flex justify-between"><span class="text-gray-400">重量:</span><span>${product.zxweight || '-'}</span></div>
                    <div class="flex justify-between"><span class="text-gray-400">起订量:</span><span>${product.MinOrderNum || '1'} ${product.unit || '件'}</span></div>
                </div>

                <div class="mt-6">
                    <h3 class="font-bold mb-2">配送与支付</h3>
                    <div class="flex items-center text-sm text-green-600 bg-green-50 p-2 rounded">
                        <svg class="w-5 h-5 mr-1" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg>
                        线下配送，无需费用
                    </div>
                </div>

                <div class="mt-6 mb-20 text-gray-600 text-sm">
                    <h3 class="font-bold mb-2">详情说明</h3>
                    <div class="prose prose-sm">${product.description || '暂无更多详细介绍。'}</div>
                </div>
            </div>
            <div class="fixed bottom-0 left-0 right-0 bg-white border-t p-3 flex space-x-3 z-50">
                <button id="detail-add-cart" class="flex-1 bg-blue-600 text-white py-3 rounded-lg font-bold">加入清单</button>
            </div>
        `;

        document.getElementById('detail-add-cart').onclick = () => {
            addToCart(product);
            alert('已加入清单');
        };
        window.scrollTo(0, 0);
    }

    function renderCart() {
        const container = document.getElementById('cart-list');
        const empty = document.getElementById('cart-empty');
        const bar = document.getElementById('checkout-bar');
        
        container.innerHTML = '';
        if (cart.size === 0) {
            empty.classList.remove('hidden');
            bar.classList.add('hidden');
            return;
        }
        
        empty.classList.add('hidden');
        bar.classList.remove('hidden');

        cart.forEach((item, id) => {
            const p = item.product;
            const div = document.createElement('div');
            div.className = 'bg-white rounded p-3 flex space-x-3 shadow-sm';
            div.innerHTML = `
                <img src="${p.sPicUrl}" referrerpolicy="no-referrer" class="w-20 h-20 object-cover rounded">
                <div class="flex-1 flex flex-col justify-between">
                    <div>
                        <h4 class="text-sm font-medium line-clamp-1">${p.ProductName}</h4>
                        <p class="text-xs text-gray-400">货号: ${p.ProModel}</p>
                    </div>
                    <div class="flex justify-between items-center">
                        <span class="text-xs text-gray-500">线下配送</span>
                        <div class="flex items-center space-x-3">
                            <button class="cart-minus w-6 h-6 border rounded flex items-center justify-center">-</button>
                            <span class="text-sm font-bold">${item.count}</span>
                            <button class="cart-plus w-6 h-6 border rounded flex items-center justify-center">+</button>
                        </div>
                    </div>
                </div>
            `;
            
            div.querySelector('.cart-minus').onclick = () => updateCartCount(id, -1);
            div.querySelector('.cart-plus').onclick = () => updateCartCount(id, 1);
            
            container.appendChild(div);
        });

        document.getElementById('cart-total-count').textContent = Array.from(cart.values()).reduce((sum, i) => sum + i.count, 0);
    }

    // --- Actions ---
    function setupEventListeners() {
        tabBtns.forEach(btn => {
            btn.addEventListener('click', () => {
                window.location.hash = btn.dataset.target;
            });
        });

        window.addEventListener('hashchange', handleRouting);

        searchBtn.onclick = performSearch;
        globalSearchInput.onkeypress = (e) => {
            if (e.key === 'Enter') performSearch();
        };

        // Infinite Scroll Observers
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    if (currentView === 'category') renderCategoryProducts();
                    if (currentView === 'search') renderSearchResults();
                }
            });
        }, { threshold: 0.1 });

        observer.observe(document.getElementById('category-scroll-trigger'));
        observer.observe(document.getElementById('search-scroll-trigger'));

        // Cart Modal
        document.getElementById('submit-order').onclick = openOrderModal;
        document.getElementById('close-modal').onclick = () => document.getElementById('order-modal').classList.add('hidden');
        document.getElementById('copy-order').onclick = copyOrderText;
    }

    function performSearch() {
        const query = globalSearchInput.value.trim();
        if (!query) return;
        window.location.hash = 'search';
        renderSearchResults(true);
    }

    function addToCart(product) {
        if (cart.has(product.id)) {
            cart.get(product.id).count++;
        } else {
            cart.set(product.id, { product, count: 1 });
        }
        updateCartBadge();
    }

    function updateCartCount(id, delta) {
        const item = cart.get(id);
        if (!item) return;
        item.count += delta;
        if (item.count <= 0) cart.delete(id);
        renderCart();
        updateCartBadge();
    }

    function updateCartBadge() {
        const total = Array.from(cart.values()).reduce((sum, i) => sum + i.count, 0);
        cartBadge.textContent = total;
        cartBadge.classList.toggle('hidden', total === 0);
    }

    function openOrderModal() {
        const summary = document.getElementById('order-summary');
        let text = `--- HDL 商城订单汇总 ---\n日期: ${new Date().toLocaleString()}\n\n`;
        let total = 0;
        cart.forEach(item => {
            text += `商品: ${item.product.ProductName}\n货号: ${item.product.ProModel}\n数量: ${item.count} ${item.product.unit || '件'}\n------------------\n`;
            total += item.count;
        });
        text += `\n总计数量: ${total}\n配送方式: 线下配送 (免运费)\n状态: 待联系客服`;
        
        summary.textContent = text;
        document.getElementById('order-modal').classList.remove('hidden');
    }

    function copyOrderText() {
        const text = document.getElementById('order-summary').textContent;
        navigator.clipboard.writeText(text).then(() => {
            alert('已复制到剪贴板，请联系客服发送。');
        });
    }

    function animateButton(btn) {
        btn.classList.add('bg-blue-600', 'text-white');
        btn.classList.remove('bg-blue-50', 'text-blue-600');
        setTimeout(() => {
            btn.classList.remove('bg-blue-600', 'text-white');
            btn.classList.add('bg-blue-50', 'text-blue-600');
        }, 300);
    }

    function showLoading() {
        const loader = document.createElement('div');
        loader.id = 'app-loader';
        loader.className = 'fixed inset-0 bg-white flex flex-col items-center justify-center z-[200]';
        loader.innerHTML = `
            <div class="w-12 h-12 border-4 border-blue-600 border-t-transparent rounded-full animate-spin mb-4"></div>
            <p class="text-gray-500 font-medium">正在初始化 30,000+ 商品数据...</p>
        `;
        document.body.appendChild(loader);
    }

    function hideLoading() {
        const loader = document.getElementById('app-loader');
        if (loader) loader.remove();
    }

    // Launch
    init();
})();
