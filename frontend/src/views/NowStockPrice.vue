<template>
	<div>
		<form @submit.prevent="now_stock_price">
			<h2>
				<label for="stock">股票名稱:&nbsp;&nbsp;&nbsp;</label>
				<input id="stock" type="text" v-model.trim="stock" />
			</h2>
			<button v-on:click="button">查詢價錢</button>
		</form>
		<hr />
		<h2>
			<div v-for="data in datas" :key="data">
				股票名稱：{{stock}} 	{{data}}
			</div>
		</h2>
		<h2><p>{{error_message}}</p></h2>
	</div>
</template>

<script>
import axios from 'axios';

export default {
	data() {
		return {
			datas: '',
			error_message: ''
		}
	},
	methods: {
		now_stock_price() {
			axios.post('http://127.0.0.1:5000/user/search', {
				stock_name: this.stock
			})
			.then(res => {
				console.log(res);
				this.datas = res.data;
				this.error_message = '';
			})
			.catch(error =>{
				if(error.response){
					if (error.response.status == 400){
						this.error_message = '請檢查股票名稱是否有誤';
						this.datas = '';
					}else if(error.response.status == 406){
						this.error_message = '請填入所有的資料';
						this.datas = '';
					}
				}else if(error.request){
					alert("沒有收到回應");
				}else{
					alert("伺服器請求失敗");
				}
			})
		},
	},
};
</script>
