<template>
    <div id="User">
        <div class="main">
            <router-view/>
        </div>
    </div>
</template>

<script>
    export default {
        name: "User",

    }
</script>

<style scoped>
    #User {
        height: 100%;
        box-sizing: border-box;

    }

    .main {
        width: 380px;
        margin: 0 auto;
        padding-top: 100px;
    }
</style>