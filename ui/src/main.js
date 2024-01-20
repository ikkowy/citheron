import { createApp } from "vue";
import { createPinia } from "pinia";
import { createRouter, createWebHashHistory } from "vue-router";
import App from "./App.vue";
import DashboardPage from "./components/DashboardPage.vue";
import LoginPage from "./components/LoginPage.vue";

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

app.mount("#app");
