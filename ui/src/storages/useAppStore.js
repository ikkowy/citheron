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
        headerForegroundColor: computed(() => darkModeEnabled.value ? "#e0e0e0" : "#101010"),
        headerHoverBackgroundColor: computed(() => darkModeEnabled.value ? "#202020" : "#d0d0d0"),
        headerMenuButtonCounterBackgroundColor: "hsla(5, 80%, 50%, 1)",
        headerMenuButtonCounterForegroundColor: "#e0e0e0",
        sideMenuBackgroundColor: computed(() => darkModeEnabled.value ? "#101010" : "#e0e0e0"),
        SideMenuEntryBackgroundColor: computed(() => darkModeEnabled.value ? "#101010" : "#e0e0e0"),
        SideMenuEntryForegroundColor: computed(() => darkModeEnabled.value ? "#ffffff" : "#101010"),
        SideMenuEntryHoverBackgroundColor: computed(() => darkModeEnabled.value ? "#202020" : "#d0d0d0"),
        mainBackgroundColor: computed(() => darkModeEnabled.value ? "#000000" : "#ffffff")
    };

    return {darkModeEnabled, theme, toggleDarkMode, setDarkMode};
});
