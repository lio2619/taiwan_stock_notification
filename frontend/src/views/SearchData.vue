<template>
	<div>
		<form @submit.prevent="search_data">
			<h2>
				<label for="email">信箱:&nbsp;&nbsp;&nbsp;</label>
				<input id="email" type="text" v-model.trim="email" />
			</h2>
			<button v-on:click="button">查詢</button>
		</form>
		<hr />
		<h2>
			<div v-for="data in all_data" :key="data">
				<div v-for="d in data" :key="d">
					股票名稱：{{d.stock_name}} 		目標價錢：{{d.target_price}}
				</div>
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
			all_data: '',
			error_message: '',
		};
	},
	methods: {
		search_data(){
			axios.post('http://127.0.0.1:5000/user/get', {
				email : this.email,
			})
			.then(res => {
				console.log(res.data);
				this.all_data = res.data;
				this.error_message = '';
			})
			.catch(error => {
				if(error.response){
					if (error.response.status == 400){
						this.error_message = '請輸入正確的信箱';
						this.all_data = '';
					}else if(error.response.status == 406){
						this.error_message = '請填入資料';
						this.all_data = '';
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
