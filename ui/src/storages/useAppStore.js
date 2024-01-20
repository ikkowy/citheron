import { computed, ref } from "vue";
import { defineStore } from "pinia";

export const useAppStore = defineStore("app", () => {
    const darkModeEnabled = ref(false);

    function toggleDarkMode() {
        darkModeEnabled.value = !darkModeEnabled.value;
        localStorage.setItem("citheron.darkModeEnabled", darkModeEnabled.value);
    }

    function setDarkMode(enabled) {
        darkModeEnabled.value = enabled;
    }

    const theme = {
        headerBackgroundColor: computed(() => darkModeEnabled.value ? "#101010" : "#e0e0e0"),
        headerForegroundColor: computed(() => darkModeEnabled.value ? "#ffffff" : "#101010"),
        headerHoverBackgroundColor: computed(() => darkModeEnabled.value ? "#202020" : "#d0d0d0"),
        headerMenuButtonCounterBackgroundColor: "#ff0000",
        headerMenuButtonCounterForegroundColor: "#ffffff",
        sideMenuBackgroundColor: computed(() => darkModeEnabled.value ? "#101010" : "#e0e0e0"),
        sideMenuButtonBackgroundColor: computed(() => darkModeEnabled.value ? "#101010" : "#e0e0e0"),
        sideMenuButtonForegroundColor: computed(() => darkModeEnabled.value ? "#ffffff" : "#101010"),
        sideMenuButtonHoverBackgroundColor: computed(() => darkModeEnabled.value ? "#202020" : "#d0d0d0"),
        mainBackgroundColor: computed(() => darkModeEnabled.value ? "#000000" : "#ffffff")
    };

    return {darkModeEnabled, theme, toggleDarkMode, setDarkMode};
});
