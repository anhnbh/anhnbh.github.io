(function () {
  var AUTH_KEY = "site_auth_v1";
  var LOGIN_TIME_KEY = "site_login_time_v1";
  var LOGIN_PAGE = "/login.html";
  var cfg = window.AUTH_CONFIG || {};
  var timeoutMs = Number(cfg.SESSION_TIMEOUT_MS || 0);

  function normalizePath(path) {
    if (!path) return "/";
    return path.replace(/\/+/g, "/");
  }

  function isAuthenticated() {
    return localStorage.getItem(AUTH_KEY) === "true";
  }

  function clearAuth() {
    localStorage.removeItem(AUTH_KEY);
    localStorage.removeItem(LOGIN_TIME_KEY);
  }

  function isSessionExpired() {
    if (!timeoutMs) return false;
    var loginTime = Number(localStorage.getItem(LOGIN_TIME_KEY) || 0);
    if (!loginTime) return true;
    return Date.now() - loginTime > timeoutMs;
  }

  function redirectToLogin() {
    var next = encodeURIComponent(window.location.pathname + window.location.search + window.location.hash);
    window.location.replace(LOGIN_PAGE + "?next=" + next);
  }

  var currentPath = normalizePath(window.location.pathname);
  var onLoginPage = currentPath === LOGIN_PAGE;

  if (isAuthenticated() && isSessionExpired()) {
    clearAuth();
  }

  if (!isAuthenticated() && !onLoginPage) {
    redirectToLogin();
    return;
  }

  if (isAuthenticated() && onLoginPage) {
    var nextParam = new URLSearchParams(window.location.search).get("next");
    if (nextParam && nextParam.startsWith("/")) {
      window.location.replace(nextParam);
    } else {
      window.location.replace(cfg.REDIRECT_AFTER_LOGIN || "/");
    }
  }
})();
