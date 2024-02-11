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

    function invertColor(hexColor) {
        const r = parseInt(hexColor.substring(1, 3), 16);
        const g = parseInt(hexColor.substring(3, 5), 16);
        const b = parseInt(hexColor.substring(5, 7), 16);
        const r_ = (255 - r).toString(16);
        const g_ = (255 - g).toString(16);
        const b_ = (255 - b).toString(16);
        return `#${r_}${g_}${b_}`;
    }

    const colDark1 = "#000000";
    const colDark2 = "#101010";
    const colDark3 = "#202020";

    const colLight1 = invertColor(colDark1);
    const colLight2 = invertColor(colDark2);
    const colLight3 = invertColor(colDark3);

    const colBg1 = computed(() => darkModeEnabled.value ? colDark1 : colLight1);
    const colBg2 = computed(() => darkModeEnabled.value ? colDark2 : colLight2);
    const colBg3 = computed(() => darkModeEnabled.value ? colDark3 : colLight3);

    const colFg1 = computed(() => darkModeEnabled.value ? colLight1 : colDark1);
    const colFg2 = computed(() => darkModeEnabled.value ? colLight2 : colDark2);
    const colFg3 = computed(() => darkModeEnabled.value ? colLight3 : colDark3);

    const colRed = "#dc0000";
    const colBlue = "#005c94";
    const colGreen = "#009100";
    const colYellow = "#ff9900";

    const theme = {
        colDark1: colDark1,
        colDark2: colDark2,
        colDark3: colDark3,

        colLight1: colLight1,
        colLight2: colLight2,
        colLight3: colLight3,

        colBg1: colBg1,
        colBg2: colBg2,
        colBg3: colBg3,

        colFg1: colFg1,
        colFg2: colFg2,
        colFg3: colFg3,

        colRed: colRed,
        colBlue: colBlue,
        colGreen: colGreen,
        colYellow: colYellow
    };

    return {darkModeEnabled, theme, toggleDarkMode, setDarkMode};
});
