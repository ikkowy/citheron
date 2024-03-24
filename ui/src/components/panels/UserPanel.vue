<script setup>
import { onMounted, ref } from "vue";

import IwyButton from "../iwy/IwyButton.vue";
import IwyGroupBox from "../iwy/IwyGroupBox.vue";
import IwyTextField from "../iwy/IwyTextField.vue";
import IwyTableView from "../iwy/IwyTableView.vue";

import DashboardPanel from "../DashboardPanel.vue";

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

  userTable.value.addRow({
    username: "helga",
    email: "helga@example.com",
    created: new Date(),
    enabled: true
  });
});
</script>

<template>
  <DashboardPanel>
    <div style="display: flex; flex-direction: column; gap: 20px">
      <div style="display: flex; flex-direction: row; flex-wrap: wrap; gap: 10px">
        <IwyTextField icon="search" button="Search" />
        <IwyButton icon="filter" label="Filter" />
        <IwyButton icon="binoculars" label="View" />
        <IwyButton icon="plus" label="Create" />
        <IwyButton icon="minus" label="Remove" />
        <IwyButton icon="export" label="Export" />
      </div>
      <IwyGroupBox title="Filter" :minimizable="true">
        Fitler stuff
      </IwyGroupBox>
      <IwyGroupBox title="View" :minimizable="true">
        View stuff
      </IwyGroupBox>
      <IwyTableView ref="userTable" :line-numbers="true" :highlight-lines="true" />
    </div>
  </DashboardPanel>
</template>

<style scoped>
</style>
