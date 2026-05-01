(function () {
  var AUTH_KEY = "site_auth_v1";
  var LOGIN_TIME_KEY = "site_login_time_v1";

  function getConfig() {
    return window.AUTH_CONFIG || {};
  }

  function isValidCredential(username, password) {
    var cfg = getConfig();
    return username === cfg.USERNAME && password === cfg.PASSWORD;
  }

  function setAuth() {
    localStorage.setItem(AUTH_KEY, "true");
    localStorage.setItem(LOGIN_TIME_KEY, String(Date.now()));
  }

  function getNextPath() {
    var next = new URLSearchParams(window.location.search).get("next");
    if (next && next.startsWith("/")) return next;
    return getConfig().REDIRECT_AFTER_LOGIN || "/";
  }

  function showError(msg) {
    var errorEl = document.getElementById("auth-error");
    if (!errorEl) return;
    errorEl.textContent = msg;
    errorEl.style.display = "block";
  }

  function clearError() {
    var errorEl = document.getElementById("auth-error");
    if (!errorEl) return;
    errorEl.textContent = "";
    errorEl.style.display = "none";
  }

  window.login = function login() {
    var userEl = document.getElementById("username");
    var passEl = document.getElementById("password");
    if (!userEl || !passEl) return;

    var username = userEl.value.trim();
    var password = passEl.value;

    if (isValidCredential(username, password)) {
      setAuth();
      window.location.replace(getNextPath());
      return;
    }

    showError("Sai tài khoản hoặc mật khẩu.");
  };

  window.logout = function logout() {
    localStorage.removeItem(AUTH_KEY);
    localStorage.removeItem(LOGIN_TIME_KEY);
    window.location.replace("/login.html");
  };

  document.addEventListener("DOMContentLoaded", function () {
    var form = document.getElementById("login-form");
    if (!form) return;

    clearError();
    form.addEventListener("submit", function (event) {
      event.preventDefault();
      window.login();
    });
  });
})();
