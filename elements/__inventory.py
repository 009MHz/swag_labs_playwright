class PageInfo:
    url = "https://www.saucedemo.com/inventory.html"
    main_display = ".inventory_container"


class Header:
    title = ".app_logo"
    burger = ".bm-burger-button"
    item_cart = "#shopping_cart_container"
    item_chart_count = ".shopping_cart_badge"


class SubHeader:
    title = ".title"

    class Filter:
        main = ".product_sort_container"
        name_asc = "option[value='az']"
        name_desc = "option[value='za']"
        price_asc = "option[value='lohi']"
        price_desc = "option[value='hilo']"


class Products:
    container = "//div[@class='inventory_item']"
    thumbnail = "//img[@class='inventory_item_img']"
    name = "//a[contains(@id, 'title_link')]"
    info = "//div[@class='inventory_item_desc']"
    price = "//div[@class='inventory_item_price']"
    add_btn = "//button[contains(@id,'add')]"
    remove_btn = "//button[contains(@id,'remove')]"


class YourCart:
    url = "https://www.saucedemo.com/cart.html"
    section_title = ".title"
    item_holder = ".cart_item_label"
    item_name = "//div[@class='inventory_item_name']"
    item_info = "//div[@class='inventory_item_desc']"
    item_price = "//div[@class='inventory_item_price']"
    item_remove = "//button[contains(@id,'remove')]"
    back_btn = "#continue-shopping"
    checkout_btn = "#checkout"


class BuyInfo:
    url = "https://www.saucedemo.com/checkout-step-one.html"
    section_title = ".title"
    main_form = ".checkout_info"
    first_name = "#first-name"
    last_name = "#last-name"
    postal = "#postal-code"
    cancel_btn = "#cancel"
    continue_btn = "#continue"


class BuyPreview:
    url = "https://www.saucedemo.com/checkout-step-two.html"
    section_title = ".title"
    item_name = "//div[@class='inventory_item_name']"
    item_info = "//div[@class='inventory_item_desc']"
    item_price = "//div[@class='inventory_item_price']"
    item_total = "div[data-test='subtotal-label']"
    summary_info = ".summary_info"
    cancel_btn = "#cancel"
    finish_btn = "#finish"


class BuyComplete:
    url = "https://www.saucedemo.com/checkout-complete.html"
    section_title = ".title"
    main_display = "#checkout_complete_container"
    header = ".complete-header"
    info = ".complete-text"
    back_home_btn = "#back-to-products"
