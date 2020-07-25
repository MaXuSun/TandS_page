<template>
    <div id="navigate">
        <el-menu class="menu_left"
                :default-active="this.$route.path"
                mode="horizontal"
                background-color="#545c64"
                text-color="#fff"
                active-text-color="#ffd04b">
            <el-submenu index="6">
                <template slot="title">退出</template>
                <el-menu-item index="5-1" @click="logoutClick">注销</el-menu-item>
                <el-menu-item index="5-2" @click="changeClick">切换账号</el-menu-item>
            </el-submenu>
            <el-menu-item index="1" @click="schClick">课表</el-menu-item>
            <el-menu-item index="3" >政策规定</el-menu-item>
            <el-menu-item index="4">
                <el-input
                        placeholder="请输入搜索内容"
                        prefix-icon="el-icon-search"/>
            </el-menu-item>
        </el-menu>
        <el-menu class="menu_right"
                 mode="horizontal"
                 background-color="#545c64"
                 text-color="#fff"
                 active-text-color="#ffd04b">
            <el-submenu index="5">
                <template slot="title">语言</template>
                <el-menu-item index="5-1">中文</el-menu-item>
                <el-menu-item index="5-2">English</el-menu-item>
            </el-submenu>
        </el-menu>
    </div>
</template>

<script>
    export default {
        name: "Navigate",
        data(){
          return{
              dialogVisible:false
          }
        },
        methods:{
            schClick(){
                this.$router.replace("/index/schedule")
            },
            logoutClick(){
                this.$confirm("确认退出?").then(()=>{
                    this.$router.replace("/user/logout")
                }).catch(()=>{

                })
            },
            changeClick(){
                this.$confirm("确认切换账号？").then(()=>{
                    this.$router.replace("/user/signin")
                }).catch(()=>{

                })
            }
        }
    }
</script>

<style scoped>
#navigate {
    width: 100%;
    background-color: #545C64;
    display: inline-block;
    border-bottom: none;
}
#navigate >>> .el-menu.el-menu--horizontal {
    border-bottom:none;
    display: inline-block;
}
.menu_left{

}
.menu_right{
    float: right;
}
</style>