import { createRouter, createWebHistory } from "vue-router";
import HomeView from "../views/HomeView.vue";

const routes = [
	{
		path: "/",
		name: "home",
		component: HomeView,
	},
	{
		path: "/about",
		name: "about",
		// route level code-splitting
		// this generates a separate chunk (about.[hash].js) for this route
		// which is lazy-loaded when the route is visited.
		component: () =>
			import(/* webpackChunkName: "about" */ "../views/AboutView.vue"),
	},
	{
		path: "/input_stock",
		component: () => import("../views/InputStockNamePage.vue"),
	},
	{
		path: "/search",
		component: () => import("../views/SearchData.vue"),
	},
	{
		path: "/update",
		component: () => import("../views/UpdateData.vue"),
	},
	{
		path: "/now",
		component: () => import("../views/NowStockPrice.vue"),
	},
	{
		//vue3變成catchAll(.*)才是抓取未定義的網頁 vue2是*
		path: "/:pathMatch(.*)",
		component: () => import("../views/NotFound.vue"),
	},
];

const router = createRouter({
	history: createWebHistory(process.env.BASE_URL),
	routes,
});

export default router;
