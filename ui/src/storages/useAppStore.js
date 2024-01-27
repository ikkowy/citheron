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

    const colDark1 = "#000000";
    const colDark2 = "#101010";
    const colDark3 = "#202020";

    const colLight1 = "#ffffff";
    const colLight2 = "#efefef";
    const colLight3 = "#dfdfdf";

    const colBg1 = computed(() => darkModeEnabled.value ? colDark1 : colLight1);
    const colBg2 = computed(() => darkModeEnabled.value ? colDark2 : colLight2);
    const colBg3 = computed(() => darkModeEnabled.value ? colDark3 : colLight3);

    const colFg1 = computed(() => darkModeEnabled.value ? colLight1 : colDark1);
    const colFg2 = computed(() => darkModeEnabled.value ? colLight2 : colDark2);
    const colFg3 = computed(() => darkModeEnabled.value ? colLight3 : colDark3);

    const colRed = "hsla(5, 80%, 50%, 1)";

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

        colRed: colRed
    };

    return {darkModeEnabled, theme, toggleDarkMode, setDarkMode};
});
