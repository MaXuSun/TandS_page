<template>
    <div id="logout">
        <div class="body">
            <div class="content">
                <span>您已经成功退出!</span>
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        name: "LogOut"
    }
</script>

<style scoped>
    #logout {
        border-radius: 4px;
        box-shadow: 0 0 8px rgba(0, 0, 0, .1);
    }

    .body {
        margin-top: 30%;
        padding: 50px 50px 70px;
        background-color: #545C64;
        border: 2px solid #545C64;
    }

    .content{
        text-align: center;
    }

    .content span{
        color: #4d79dd;
        font-size: 40px;
    }
</style>