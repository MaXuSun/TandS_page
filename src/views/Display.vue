<template>
    <div>
        <Navigate/>
        <router-view/>
    </div>
</template>

<script>
    import Navigate from "@/components/Navigate";
    export default {
        name: "Display",
        components:{Navigate}
    }
</script>

<style scoped>

</style>