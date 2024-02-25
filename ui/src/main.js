import "./assets/style.css";

import { createApp } from "vue";
import { createPinia } from "pinia";
import { createRouter, createWebHashHistory } from "vue-router";
import App from "./App.vue";
import DashboardPage from "./components/DashboardPage.vue";
import LoginPage from "./components/LoginPage.vue";

import IwyIconsVue from "@ikkowy/icons-vue";

const pinia = createPinia();

const routes = [
  { path: "/", component: DashboardPage },
  { path: "/login", component: LoginPage }
];

const router = createRouter({
  history: createWebHashHistory(),
  routes: routes,
  linkActiveClass: "active"
});

const app = createApp(App);

app.use(pinia);

app.use(router);

app.use(IwyIconsVue);

app.mount("#app");

import { useAppStore } from "@/storages/useAppStore";
const appStore = useAppStore();
const { setDarkMode } = appStore;

const isDarkModeEnabled = localStorage.getItem("citheron.darkModeEnabled");
if (isDarkModeEnabled !== null) {
  setDarkMode(isDarkModeEnabled === "true");
} else if (window.matchMedia && window.matchMedia("(prefers-color-scheme: dark)").matches) {
  setDarkMode(true);
}
