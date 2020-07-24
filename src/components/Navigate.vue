<template>
    <div>
        <el-menu
                mode="horizontal"
                background-color="#545c64"
                text-color="#fff"
                :router="true"
                active-text-color="#ffd04b">
            <el-menu-item index="/index/schedule">课表</el-menu-item>
            <el-menu-item index="3" >政策/规定</el-menu-item>
            <el-submenu index="5">
                <template slot="title">语言</template>
                <el-menu-item index="5-1">中文</el-menu-item>
                <el-menu-item index="5-2">English</el-menu-item>
            </el-submenu>
            <el-submenu index="6">
                <template slot="title">退出</template>
                <el-menu-item index="5-1">注销</el-menu-item>
                <el-menu-item index="5-2">切换账号</el-menu-item>
            </el-submenu>
            <el-menu-item index="4">
                <el-input
                        placeholder="请输入搜索内容"
                        prefix-icon="el-icon-search"/>
            </el-menu-item>
        </el-menu>
    </div>
</template>

<script>
    export default {
        name: "Navigate"
    }
</script>

<style scoped>

</style>