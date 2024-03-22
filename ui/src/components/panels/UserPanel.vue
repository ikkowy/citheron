<script setup>
import { onMounted, ref } from "vue";

import IwyButton from "../iwy/IwyButton.vue";
import IwyTextField from "../iwy/IwyTextField.vue";
import IwyTableView from "../iwy/IwyTableView.vue";

import DashboardPanel from "../DashboardPanel.vue";

import { useAppStore } from "@/storages/useAppStore";
const appStore = useAppStore();
const { theme } = appStore;

const userTable = ref(null);

onMounted(() => {
  userTable.value.addColumn("username");
  userTable.value.addColumn("email");
  userTable.value.addColumn("created");
  userTable.value.addColumn("enabled");

  userTable.value.addRow({
    username: "vincent",
    email: "vincent@example.com",
    created: new Date(),
    enabled: true
  });
});
</script>

<template>
  <DashboardPanel>
    <div style="display: flex; flex-direction: column; gap: 10px">
      <div style="display: flex; flex-direction: row; gap: 10px">
        <IwyTextField icon="search" button="Search" />
        <IwyButton icon="filter" label="Filter" />
        <IwyButton icon="plus" label="Create" />
        <IwyButton icon="minus" label="Remove" />
        <IwyButton icon="export" label="Export" />
      </div>
      <IwyTableView ref="userTable" />
    </div>
  </DashboardPanel>
</template>

<style scoped>
</style>
