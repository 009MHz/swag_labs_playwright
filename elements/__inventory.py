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
