<template>
    <div id="logout">
        <el-dialog
                :title=eltitle
                :visible.sync="dialogVisible"
                width="30%"
                :before-close="handleClose">
            <span>{{this.$t('msg.msgout')}}</span>
            <span slot="footer" class="dialog-footer">
                <el-button type="primary" @click="handleClose">{{$t('msg.ok')}}</el-button>
          </span>
        </el-dialog>
    </div>
</template>

<script>
    export default {
        name: "LogOut",
        data() {
            return {
                dialogVisible: true,
                eltitle:this.$t('msg.notice'),
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