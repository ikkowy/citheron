import { ref, computed } from "vue";

export const darkModeEnabled = ref(false);

export const theme = {
    headerBackgroundColor: "#1a1a1a",
    headerForegroundColor: "#d9d9d9",
    headerHoverBackgroundColor: "#262626",
    sideMenuBackgroundColor: "#1a1a1a",
    sideMenuButtonBackgroundColor: "#1a1a1a",
    sideMenuButtonForegroundColor: "#d9d9d9",
    sideMenuButtonHoverBackgroundColor: "#262626",
    mainBackgroundColor: computed(() => darkModeEnabled.value ? "#000000" : "#ffffff")
};
