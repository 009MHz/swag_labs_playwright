class PageInfo:
    url = "https://www.saucedemo.com/inventory.html"
    main_display = ".inventory_container"


class Header:
    title = ".app_logo"
    burger = ".bm-burger-button"
    shop_chart = "#shopping_cart_container"


class SubHeader:
    title = ".title"

    class Filter:
        main = ".product_sort_container"
        name_asc = "option[value='az']"
        name_desc = "option[value='za']"
        price_asc = "option[value='lohi']"
        price_desc = "option[value='hilo']"


class MainForm:
    user_name = "#user-name"
    password = "#password"
    login_btn = "#login-button"


class FormInfo:
    user_form = "#login_credentials"
    user_header = "div[id='login_credentials'] h4"

    pass_form = ".login_password"
    pass_header = "div[class='login_password'] h4"

