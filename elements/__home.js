class PageInfo {
    static url = "https://www.saucedemo.com/";
    static title = ".login_logo";
}

class MainForm {
    static userName = "#user-name";
    static userNameXPath = "//input[@data-test='username']";
    static password = "#password";
    static passwordXPath = "//input[@name='password']";
    static loginButton = "#login-button";
    static loginButtonXPath = "//input[@name='login-button']";
}

module.exports = { PageInfo, MainForm };
