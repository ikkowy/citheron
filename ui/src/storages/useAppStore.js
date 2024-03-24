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

    // function invertColor(hexColor) {
    //     const r = parseInt(hexColor.substring(1, 3), 16);
    //     const g = parseInt(hexColor.substring(3, 5), 16);
    //     const b = parseInt(hexColor.substring(5, 7), 16);
    //     const r_ = (255 - r).toString(16);
    //     const g_ = (255 - g).toString(16);
    //     const b_ = (255 - b).toString(16);
    //     return `#${r_}${g_}${b_}`;
    // }

    const colBg = computed(() => darkModeEnabled.value ? "black" : "white");

    const colFg = computed(() => darkModeEnabled.value ? "white" : "black");

    const colRed = "#dc0000";
    const colBlue = "#005c94";
    const colGreen = "#009100";
    const colYellow = "#ff9900";

    const theme = {
        colBg: colBg,
        colFg: colFg,
        colRed: colRed,
        colBlue: colBlue,
        colGreen: colGreen,
        colYellow: colYellow
    };

    return {darkModeEnabled, theme, toggleDarkMode, setDarkMode};
});
