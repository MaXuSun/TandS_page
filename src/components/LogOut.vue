<template>
    <div id="logout">
        <el-dialog
                title="提示"
                :visible.sync="dialogVisible"
                width="30%"
                :before-close="handleClose">
            <span>您已经成功退出！</span>
            <span slot="footer" class="dialog-footer">
                <el-button type="primary" @click="handleClose">确 定</el-button>
          </span>
        </el-dialog>
    </div>
</template>

<script>
    export default {
        name: "LogOut",
        data() {
            return {
                dialogVisible: true
            };
        },
        methods: {
            handleClose() {
                this.$router.replace("/user/signin")
            }
        }
    }
</script>

<style scoped>

</style>