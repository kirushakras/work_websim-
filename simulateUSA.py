from worldquant.simulate.parallel import simulate_many
from worldquant.api import WQClient
from worldquant.exceptions import WQException
import random
import os

user = 'nepishiemy@yandex.ru'
pswd = 'Peresvet1488'
client = WQClient()
client.login(user, pswd)
print("authorization successful")


funda        = ["assets","assets_curr","bookvalue_ps","capex","cash","cashflow","cashflow_dividends","cashflow_fin","cashflow_invst","cashflow_op","cogs","current_ratio","debt","debt_lt","debt_st","depre_amort","EBIT","EBITDA","employee","enterprise_value","eps","equity","goodwill","income","income_beforeextra","income_tax","interest_expense","inventory","inventory_turnover","invested_capital","liabilities","liabilities_curr","operating_expense","operating_income","ppent","pretax_income","receivable","retained_earnings","return_assets","return_equity","revenue","sales","sales_growth","sales_ps","SGA_expense","working_capital"]
PriceVolume = ["open","close","high","low","vwap","volume","returns","adv20","cap"]
USNewsData  = ["news_prev_vol","news_curr_vol","news_mov_vol","news_ratio_vol","news_open_vol","news_close_vol","news_tot_ticks","news_atr14","news_prev_day_ret","news_prev_close","news_open","news_spy_last","news_ton_high","news_ton_low","news_ton_last","news_eod_high","news_eod_low","news_eod_close","news_spy_close","news_post_vwap","news_pre_vwap","news_main_vwap","news_all_vwap","news_eod_vwap","news_max_up_amt","news_max_up_ret","news_max_dn_amt","news_max_dn_ret","news_session_range","news_session_range_pct","news_ls","news_indx_perf","news_pct_1min","news_pct_5_min","news_pct_10min","news_pct_30min","news_pct_60min","news_pct_90min","news_pct_120min","news_mins_1_chg","news_cap","news_pe_ratio","news_dividend_yield","news_short_interest","news_high_exc_stddev","news_low_exc_stddev","news_vol_stddev","news_range_stddev","news_atr_ratio"]
AnalystRevisionScore    = ["star_arm_score","star_arm_score_5","star_arm_global_rank","star_arm_country_rank","star_arm_pref_earnings_score","star_arm_recommendations_score","star_arm_revenue_score","star_arm_secondary_earnings_score","star_arm_score_change_1m","star_arm_region_rank_decimal"]
EPSEstimateModel        = ["star_eps_analyst_number_fq1","star_eps_analyst_number_fq2","star_eps_analyst_number_fy1","star_eps_analyst_number_fy2","star_eps_fq1_enddate","star_eps_fq2_enddate","star_eps_fy1_enddate","star_eps_fy2_enddate","star_eps_surprise_prediction_fq1","star_eps_surprise_prediction_fq2","star_eps_surprise_prediction_fy1","star_eps_surprise_prediction_fy2","star_eps_smart_estimate_fq1","star_eps_smart_estimate_fq2","star_eps_smart_estimate_fy1","star_eps_smart_estimate_fy2","star_eps_surprise_prediction_12m","star_eps_smart_estimate_12m"]
CreditRiskModel         = ["star_ccr_country_rank","star_ccr_global_rank","star_ccr_implied_rating","star_ccr_industry_rank","star_ccr_combined_pd","star_ccr_region_rank","star_ccr_sector_rank"]
PriceMomentumModel      = ["star_pm_global_rank","star_pm_industry","star_pm_longterm","star_pm_midterm","star_pm_region_rank","star_pm_shortterm"]
RevenueEstimate         = ["star_rev_analyst_number_fq1","star_rev_analyst_number_fq2","star_rev_analyst_number_fy1","star_rev_analyst_number_fy2","star_rev_fq1_enddate","star_rev_fq2_enddate","star_rev_fy1_enddate","star_rev_fy2_enddate","star_rev_surprise_prediction_12m","star_rev_surprise_prediction_fq1","star_rev_surprise_prediction_fq2","star_rev_surprise_prediction_fy1","star_rev_surprise_prediction_fy2","star_rev_smart_estimate_12m","star_rev_smart_estimate_fq1","star_rev_smart_estimate_fq2","star_rev_smart_estimate_fy1", "star_rev_smart_estimate_fy2"]

Estimate        = ["est_bookvalue_ps","est_capex","est_cashflow_fin","est_cashflow_invst","est_cashflow_op","est_cashflow_ps","est_dividend_ps","est_ebit","est_ebitda","est_eps","est_epsr","est_fcf","est_fcf_ps","est_grossincome","est_netdebt","est_netprofit","est_netprofit_adj","est_ptp","est_ptpr","est_rd_expense","est_sales","est_sga","est_shequity","est_tbv_ps","est_tot_assets","est_tot_goodwill","etz_eps","etz_eps_delta","etz_eps_ret","etz_eps_tsrank","etz_revenue","etz_revenue_delta","etz_revenue_ret"]
Relationship    = ["rel_num_all","rel_num_comp","rel_num_cust","rel_num_part","rel_ret_all","rel_ret_comp","rel_ret_cust","rel_ret_part"]
Sentiment       = ["snt_bearish","snt_bearish_tsrank","snt_bullish","snt_bullish_tsrank","snt_buzz","snt_buzz_bfl","snt_buzz_ret","snt_ratio_tsrank","snt_social_value","snt_social_volume","snt_value"]
mdf       = ["mdf_cap","mdf_fnl","mdf_inv_q","mdf_pay_q","mdf_pmo","mdf_sti_q","mdf_cex_q","mdf_cfa_q","mdf_cfi_q","mdf_com","mdf_cse","mdf_dep","mdf_dep_q","mdf_fii","mdf_ite_q","mdf_mfq","mdf_pay","mdf_pbk","mdf_peg","mdf_per","mdf_ppe_q","mdf_prm","mdf_pva","mdf_pvr","mdf_rcv","mdf_rcv_q","mdf_rev","mdf_rte_q","mdf_sal","mdf_shr","mdf_sph","mdf_spm","mdf_std","mdf_std_q","mdf_sti","mdf_tax","mdf_tca_q","mdf_trr","mdf_val","mdf_vmo","mdf_bso","mdf_bso_q","mdf_ceq","mdf_cex","mdf_cfa","mdf_cfi","mdf_cse_q","mdf_das","mdf_ebt","mdf_ebt_q","mdf_eda","mdf_emo","mdf_eup","mdf_gpr","mdf_ibt","mdf_ibt_q","mdf_iex_q","mdf_inv","mdf_ita","mdf_ite","mdf_nco_q","mdf_net","mdf_net_q","mdf_oin","mdf_oin_q","mdf_pcf","mdf_peh","mdf_plc","mdf_rec","mdf_roi","mdf_rte","mdf_sed","mdf_sga","mdf_smo","mdf_tcl_q","mdf_ato","mdf_bsd","mdf_cne","mdf_csh_q","mdf_isd","mdf_ldt","mdf_mfy","mdf_nco","mdf_rac","mdf_roe","mdf_sdr","mdf_eno","mdf_grm","mdf_gro","mdf_gwl_q","mdf_iex","mdf_ito","mdf_ldt_q","mdf_odl","mdf_pec","mdf_ppe","mdf_pvh","mdf_rev_q","mdf_cfl","mdf_ebm","mdf_edv","mdf_efy","mdf_gwl","mdf_ltd","mdf_plb","mdf_tcl","mdf_deq","mdf_grp","mdf_pss","mdf_shb","mdf_avi","mdf_div","mdf_fnd","mdf_inb","mdf_ass","mdf_csh","mdf_gpr_q","mdf_ita_q","mdf_qty","mdf_tca","mdf_cps","mdf_dpr","mdf_tie","mdf_coa","mdf_coa_q","mdf_gry","mdf_pre","mdf_exi","mdf_oey","mdf_bsd_q","mdf_ccc_q","mdf_tas_q","mdf_atr","mdf_isd_q","mdf_nps","mdf_era","mdf_pra","mdf_yld","mdf_tli_q"]
SystematicRiskMetrics = ["beta_last_30_days_spy","beta_last_60_days_spy","beta_last_90_days_spy","beta_last_360_days_spy","correlation_last_30_days_spy","correlation_last_60_days_spy","correlation_last_90_days_spy","correlation_last_360_days_spy","systematic_risk_last_30_days","systematic_risk_last_60_days","systematic_risk_last_90_days","systematic_risk_last_360_days","unsystematic_risk_last_30_days","unsystematic_risk_last_60_days","unsystematic_risk_last_90_days","unsystematic_risk_last_360_days"]
StreetEvents = ["se_event_count","se_neg_words","se_pos_words","se_neg_score","se_pos_score","se_score"]
ShortInterestModel  = ["star_si_insown_pct","star_si_country_rank","star_si_cap_rank","star_si_sector_rank","star_si_country_rank_unadj","star_si_shortsqueeze_rank"]
VolatilityData      = ["historical_volatility_10","historical_volatility_20","historical_volatility_30","historical_volatility_60","historical_volatility_90","historical_volatility_120","historical_volatility_150","historical_volatility_180","implied_volatility_call_10","implied_volatility_call_20","implied_volatility_call_30","implied_volatility_call_60","implied_volatility_call_90","implied_volatility_call_120","implied_volatility_call_150","implied_volatility_call_180","implied_volatility_call_270","implied_volatility_call_360","implied_volatility_call_720","implied_volatility_call_1080","implied_volatility_mean_10","implied_volatility_mean_20","implied_volatility_mean_30","implied_volatility_mean_60","implied_volatility_mean_90","implied_volatility_mean_120","implied_volatility_mean_150","implied_volatility_mean_180","implied_volatility_mean_270","implied_volatility_mean_360","implied_volatility_mean_720","implied_volatility_mean_1080","implied_volatility_mean_skew_10","implied_volatility_mean_skew_20","implied_volatility_mean_skew_30","implied_volatility_mean_skew_60","implied_volatility_mean_skew_90","implied_volatility_mean_skew_120","implied_volatility_mean_skew_150","implied_volatility_mean_skew_180","implied_volatility_mean_skew_270","implied_volatility_mean_skew_360","implied_volatility_mean_skew_720","implied_volatility_mean_skew_1080","implied_volatility_put_10","implied_volatility_put_20","implied_volatility_put_30","implied_volatility_put_60","implied_volatility_put_90","implied_volatility_put_120","implied_volatility_put_150","implied_volatility_put_180","implied_volatility_put_270","implied_volatility_put_360","implied_volatility_put_720","implied_volatility_put_1080","parkinson_volatility_10","parkinson_volatility_20","parkinson_volatility_30","parkinson_volatility_60","parkinson_volatility_90","parkinson_volatility_120","parkinson_volatility_150","parkinson_volatility_180"]
OptionsAnalytics    = ["call_breakeven_10","call_breakeven_20","call_breakeven_30","call_breakeven_60","call_breakeven_90","call_breakeven_120","call_breakeven_150","call_breakeven_180","call_breakeven_270","call_breakeven_360","call_breakeven_720","call_breakeven_1080","forward_price_10","forward_price_20","forward_price_30","forward_price_60","forward_price_90","forward_price_120","forward_price_150","forward_price_180","forward_price_270","forward_price_360","forward_price_720","forward_price_1080","option_breakeven_10","option_breakeven_20","option_breakeven_30","option_breakeven_60","option_breakeven_90","option_breakeven_120","option_breakeven_150","option_breakeven_180","option_breakeven_270","option_breakeven_360","option_breakeven_720","option_breakeven_1080","pcr_oi_10","pcr_oi_20","pcr_oi_30","pcr_oi_60","pcr_oi_90","pcr_oi_120","pcr_oi_150","pcr_oi_180","pcr_oi_270","pcr_oi_360","pcr_oi_720","pcr_oi_1080","pcr_oi_all","pcr_vol_10","pcr_vol_20","pcr_vol_30","pcr_vol_60","pcr_vol_90","pcr_vol_120","pcr_vol_150","pcr_vol_180","pcr_vol_270","pcr_vol_360","pcr_vol_720","pcr_vol_1080","pcr_vol_all","put_breakeven_10","put_breakeven_20","put_breakeven_30","put_breakeven_60","put_breakeven_90","put_breakeven_120","put_breakeven_150","put_breakeven_180","put_breakeven_270","put_breakeven_360","put_breakeven_720","put_breakeven_1080"]
InsiderModelData    = ["star_in_country_rank","star_in_industry_rank","star_in_sector_rank","star_in_netbuyer_ratio_rank","star_in_purchase_depth_rank","star_in_selling_depth_rank"]
SmartHoldingsModel      = ["star_hold_global_change_rank","star_hold_region_change_rank","star_hold_country_rank","star_hold_global_rank","star_hold_industry_rank","star_hold_global_owner_rank","star_hold_region_owner_rank","star_hold_region_rank","star_hold_global_screening_rank","star_hold_region_screening_rank","star_hold_sector_rank"]
SmartRatiosModel        = ["star_sr_global_rank","star_sr_liquidity","star_sr_region_rank","star_sr_sector_rank","star_sr_industr_rank","star_sr_country_rank","star_sr_growth","star_sr_profitability","star_sr_leverage","star_sr_coverage"]
GrowthValuationModel    = ["star_val_dividend_projection_fy1","star_val_dividend_projection_fy2","star_val_dividend_projection_fy3","star_val_dividend_projection_fy4","star_val_dividend_projection_fy5","star_val_dividend_projection_fy6","star_val_dividend_projection_fy7","star_val_dividend_projection_fy8","star_val_dividend_projection_fy9","star_val_dividend_projection_fy10","star_val_dividend_projection_fy11","star_val_dividend_projection_fy12","star_val_dividend_projection_fy13","star_val_dividend_projection_fy14","star_val_dividend_projection_fy15","star_val_earnings_measure_type","star_val_earnings_projection_fy1","star_val_earnings_projection_fy2","star_val_earnings_projection_fy3","star_val_earnings_projection_fy4","star_val_earnings_projection_fy5","star_val_earnings_projection_fy6","star_val_earnings_projection_fy7","star_val_earnings_projection_fy8","star_val_earnings_projection_fy9","star_val_earnings_projection_fy10","star_val_earnings_projection_fy11","star_val_earnings_projection_fy12","star_val_earnings_projection_fy13","star_val_earnings_projection_fy14","star_val_earnings_projection_fy15","star_val_fwd10_eps_cagr","star_val_fwd5_eps_cagr","star_val_fy_end_date","star_val_implied10_eps_cagr","star_val_implied5_eps_cagr","star_val_iv_projection","star_val_piv_ratio","star_val_piv_industry_rank","star_val_piv_region_rank","star_val_piv_sector_rank","star_val_buyback_yield","star_val_dividend_yield","star_val_ev_sales","star_val_industry_rank","star_val_pb","star_val_pcf","star_val_pe","star_val_region_rank","star_val_sector_rank"]

AnalystRevisions                 = ["star_arm_rec_change_flag","star_arm_rec_days_since_2lv_change","star_arm_rec_days_since_new","star_arm_rec_days_since_newsell","star_arm_rec_ndown_30","star_arm_rec_nup_30","star_arm_rec_mean_change30","star_arm_rec_mean_prior7"]
VolatilityandRiskFactorData      = ["qs_alpha_1d","qs_beta_1d","qs_fdim_1d","qs_hurst_1d","qs_kurt_1d","qs_mom3_1d","qs_mom4_1d","qs_ret_1d","qs_skew_1d","qs_var_1d","qs_alpha_5d","qs_beta_5d","qs_fdim_5d","qs_hurst_5d","qs_kurt_5d","qs_mom3_5d","qs_mom4_5d","qs_ret_5d","qs_skew_5d","qs_var_5d","qs_alpha_22d","qs_beta_22d","qs_fdim_22d","qs_hurst_22d","qs_kurt_22d","qs_mom3_22d","qs_mom4_22d","qs_ret_22d","qs_skew_22d","qs_var_22d"]
EBITDAEstimateModel                = ["star_ebitda_analyst_number_fq1","star_ebitda_fq1_enddate","star_ebitda_surprise_prediction_fq1","star_ebitda_smart_estimate_fq1","star_ebitda_analyst_number_fq2","star_ebitda_fq2_enddate","star_ebitda_surprise_prediction_fq2","star_ebitda_smart_estimate_fq2","star_ebitda_analyst_number_fy1","star_ebitda_fy1_enddate","star_ebitda_surprise_prediction_fy1","star_ebitda_smart_estimate_fy1","star_ebitda_analyst_number_fy2","star_ebitda_fy2_enddate","star_ebitda_surprise_prediction_fy2","star_ebitda_smart_estimate_fy2","star_ebitda_analyst_number_12m","star_ebitda_12m_enddate","star_ebitda_surprise_prediction_12m","star_ebitda_smart_estimate_12m"]


AnalystRevisionScore  = ["star_arm_score","star_arm_score_5","star_arm_global_rank","star_arm_country_rank","star_arm_pref_earnings_score","star_arm_recommendations_score","star_arm_revenue_score","star_arm_secondary_earnings_score","star_arm_score_change_1m","star_arm_region_rank_decimal"]
EPSEstimateModel = ["star_eps_analyst_number_fq1","star_eps_analyst_number_fq2","star_eps_analyst_number_fy1","star_eps_analyst_number_fy2","star_eps_fq1_enddate","star_eps_fq2_enddate","star_eps_fy1_enddate","star_eps_fy2_enddate","star_eps_surprise_prediction_fy1","star_eps_surprise_prediction_fy2","star_eps_smart_estimate_fq1","star_eps_smart_estimate_fq2","star_eps_smart_estimate_fy1","star_eps_smart_estimate_fy2"]
CreditRiskModel = ["star_ccr_country_rank","star_ccr_global_rank","star_ccr_implied_rating","star_ccr_industry_rank","star_ccr_combined_pd","star_ccr_region_rank","star_ccr_sector_rank"]
PriceMomentumModel = ["star_pm_global_rank","star_pm_industry","star_pm_longterm","star_pm_midterm","star_pm_region_rank","star_pm_shortterm"]
RevenueEstimate = ["star_rev_analyst_number_fq1","star_rev_analyst_number_fq2","star_rev_analyst_number_fy1","star_rev_analyst_number_fy2","star_rev_fq1_enddate","star_rev_fq2_enddate","star_rev_fy1_enddate","star_rev_fy2_enddate","star_rev_surprise_prediction_12m","star_rev_surprise_prediction_fq1","star_rev_surprise_prediction_fq2","star_rev_surprise_prediction_fy1","star_rev_surprise_prediction_fy2","star_rev_smart_estimate_12m","star_rev_smart_estimate_fq1","star_rev_smart_estimate_fq2","star_rev_smart_estimate_fy1"]
GrowthValuationModel = ["star_val_earnings_measure_type","star_val_fwd10_eps_cagr","star_val_fwd5_eps_cagr","star_val_fy_end_date","star_val_implied10_eps_cagr","star_val_implied5_eps_cagr","star_val_iv_projection","star_val_piv_ratio","star_val_piv_industry_rank","star_val_piv_region_rank","star_val_piv_sector_rank","star_val_buyback_yield","star_val_dividend_yield","star_val_ev_sales","star_val_industry_rank","star_val_pb","star_val_pcf","star_val_pe","star_val_region_rank","star_val_sector_rank"]
name = ["star_sr_global_rank","star_sr_liquidity","star_sr_region_rank","star_sr_sector_rank","star_sr_industr_rank","star_sr_country_rank","star_sr_growth","star_sr_profitability","star_sr_leverage","star_sr_coverage"]
AnalystRevisions  =  ["star_arm_rec_change_flag","star_arm_rec_days_since_2lv_change","star_arm_rec_days_since_new","star_arm_rec_days_since_newsell","star_arm_rec_ndown_30","star_arm_rec_nup_30","star_arm_rec_mean_change30","star_arm_rec_mean_prior7"]
EBITDAEstimateModel = ["star_ebitda_analyst_number_fq1","star_ebitda_fq1_enddate","star_ebitda_surprise_prediction_fq1","star_ebitda_smart_estimate_fq1","star_ebitda_analyst_number_fq2","star_ebitda_fq2_enddate","star_ebitda_surprise_prediction_fq2","star_ebitda_smart_estimate_fq2","star_ebitda_analyst_number_fy1","star_ebitda_fy1_enddate","star_ebitda_surprise_prediction_fy1","star_ebitda_smart_estimate_fy1","star_ebitda_analyst_number_fy2","star_ebitda_fy2_enddate","star_ebitda_surprise_prediction_fy2","star_ebitda_smart_estimate_fy2","star_ebitda_surprise_prediction_12m","star_ebitda_smart_estimate_12m"]
io = ["io_inst_holding","io_inst_prev_holding","io_inst_mv","io_inst_prev_mv","io_inst_pct","io_inst_number","io_fund_holding","io_fund_prev_holding","io_fund_mv","io_fund_prev_mv","io_fund_pct","io_fund_number"]
PT = ["rtk_ptg_high","rtk_ptg_low","rtk_ptg_mean","rtk_ptg_median","rtk_ptg_stddev","rtk_ptg_number"]


alphas = []
tipeofdata = [["star_ebitda_analyst_number_fq1","star_ebitda_fq1_enddate","star_ebitda_surprise_prediction_fq1","star_ebitda_smart_estimate_fq1","star_ebitda_analyst_number_fq2","star_ebitda_fq2_enddate","star_ebitda_surprise_prediction_fq2","star_ebitda_smart_estimate_fq2","star_ebitda_analyst_number_fy1","star_ebitda_fy1_enddate","star_ebitda_surprise_prediction_fy1","star_ebitda_smart_estimate_fy1","star_ebitda_analyst_number_fy2","star_ebitda_fy2_enddate","star_ebitda_surprise_prediction_fy2","star_ebitda_smart_estimate_fy2","star_ebitda_surprise_prediction_12m","star_ebitda_smart_estimate_12m"],["star_arm_rec_change_flag","star_arm_rec_days_since_2lv_change","star_arm_rec_days_since_new","star_arm_rec_days_since_newsell","star_arm_rec_ndown_30","star_arm_rec_nup_30","star_arm_rec_mean_change30","star_arm_rec_mean_prior7"],["star_sr_global_rank","star_sr_liquidity","star_sr_region_rank","star_sr_sector_rank","star_sr_industr_rank","star_sr_country_rank","star_sr_growth","star_sr_profitability","star_sr_leverage","star_sr_coverage"],["star_val_earnings_measure_type","star_val_fwd10_eps_cagr","star_val_fwd5_eps_cagr","star_val_fy_end_date","star_val_implied10_eps_cagr","star_val_implied5_eps_cagr","star_val_iv_projection","star_val_piv_ratio","star_val_piv_industry_rank","star_val_piv_region_rank","star_val_piv_sector_rank","star_val_buyback_yield","star_val_dividend_yield","star_val_ev_sales","star_val_industry_rank","star_val_pb","star_val_pcf","star_val_pe","star_val_region_rank","star_val_sector_rank"],["star_rev_analyst_number_fq1","star_rev_analyst_number_fq2","star_rev_analyst_number_fy1","star_rev_analyst_number_fy2","star_rev_fq1_enddate","star_rev_fq2_enddate","star_rev_fy1_enddate","star_rev_fy2_enddate","star_rev_surprise_prediction_12m","star_rev_surprise_prediction_fq1","star_rev_surprise_prediction_fq2","star_rev_surprise_prediction_fy1","star_rev_surprise_prediction_fy2","star_rev_smart_estimate_12m","star_rev_smart_estimate_fq1","star_rev_smart_estimate_fq2","star_rev_smart_estimate_fy1"],["star_pm_global_rank","star_pm_industry","star_pm_longterm","star_pm_midterm","star_pm_region_rank","star_pm_shortterm"],["star_ccr_country_rank","star_ccr_global_rank","star_ccr_implied_rating","star_ccr_industry_rank","star_ccr_combined_pd","star_ccr_region_rank","star_ccr_sector_rank"],["star_eps_analyst_number_fq1","star_eps_analyst_number_fq2","star_eps_analyst_number_fy1","star_eps_analyst_number_fy2","star_eps_fq1_enddate","star_eps_fq2_enddate","star_eps_fy1_enddate","star_eps_fy2_enddate","star_eps_surprise_prediction_fy1","star_eps_surprise_prediction_fy2","star_eps_smart_estimate_fq1","star_eps_smart_estimate_fq2","star_eps_smart_estimate_fy1","star_eps_smart_estimate_fy2"],["star_arm_score","star_arm_score_5","star_arm_global_rank","star_arm_country_rank","star_arm_pref_earnings_score","star_arm_recommendations_score","star_arm_revenue_score","star_arm_secondary_earnings_score","star_arm_score_change_1m","star_arm_region_rank_decimal"],["io_inst_holding","io_inst_prev_holding","io_inst_mv","io_inst_prev_mv","io_inst_pct","io_inst_number","io_fund_holding","io_fund_prev_holding","io_fund_mv","io_fund_prev_mv","io_fund_pct","io_fund_number"]]
classic =[["assets","assets_curr","bookvalue_ps","capex","cash","cashflow","cashflow_dividends","cashflow_fin","cashflow_invst","cashflow_op","cogs","current_ratio","debt","debt_lt","debt_st","depre_amort","EBIT","EBITDA","employee","enterprise_value","eps","equity","goodwill","income","income_beforeextra","income_tax","interest_expense","inventory","inventory_turnover","invested_capital","liabilities","liabilities_curr","operating_expense","operating_income","ppent","pretax_income","receivable","retained_earnings","return_assets","return_equity","revenue","sales","sales_growth","sales_ps","SGA_expense","working_capital"], ["est_bookvalue_ps","est_capex","est_cashflow_fin","est_cashflow_invst","est_cashflow_op","est_cashflow_ps","est_dividend_ps","est_ebit","est_ebitda","est_eps","est_epsr","est_fcf","est_fcf_ps","est_grossincome","est_netdebt","est_netprofit","est_netprofit_adj","est_ptp","est_ptpr","est_rd_expense","est_sales","est_sga","est_shequity","est_tbv_ps","est_tot_assets","est_tot_goodwill","etz_eps","etz_eps_delta","etz_eps_ret","etz_eps_tsrank","etz_revenue","etz_revenue_delta","etz_revenue_ret"],["mdf_cap","mdf_fnl","mdf_inv_q","mdf_pay_q","mdf_pmo","mdf_sti_q","mdf_cex_q","mdf_cfa_q","mdf_cfi_q","mdf_com","mdf_cse","mdf_dep","mdf_dep_q","mdf_fii","mdf_ite_q","mdf_mfq","mdf_pay","mdf_pbk","mdf_peg","mdf_per","mdf_ppe_q","mdf_prm","mdf_pva","mdf_pvr","mdf_rcv","mdf_rcv_q","mdf_rev","mdf_rte_q","mdf_sal","mdf_shr","mdf_sph","mdf_spm","mdf_std","mdf_std_q","mdf_sti","mdf_tax","mdf_tca_q","mdf_trr","mdf_val","mdf_vmo","mdf_bso","mdf_bso_q","mdf_ceq","mdf_cex","mdf_cfa","mdf_cfi","mdf_cse_q","mdf_das","mdf_ebt","mdf_ebt_q","mdf_eda","mdf_emo","mdf_eup","mdf_gpr","mdf_ibt","mdf_ibt_q","mdf_iex_q","mdf_inv","mdf_ita","mdf_ite","mdf_nco_q","mdf_net","mdf_net_q","mdf_oin","mdf_oin_q","mdf_pcf","mdf_peh","mdf_plc","mdf_rec","mdf_roi","mdf_rte","mdf_sed","mdf_sga","mdf_smo","mdf_tcl_q","mdf_ato","mdf_bsd","mdf_cne","mdf_csh_q","mdf_isd","mdf_ldt","mdf_mfy","mdf_nco","mdf_rac","mdf_roe","mdf_sdr","mdf_eno","mdf_grm","mdf_gro","mdf_gwl_q","mdf_iex","mdf_ito","mdf_ldt_q","mdf_odl","mdf_pec","mdf_ppe","mdf_pvh","mdf_rev_q","mdf_cfl","mdf_ebm","mdf_edv","mdf_efy","mdf_gwl","mdf_ltd","mdf_plb","mdf_tcl","mdf_deq","mdf_grp","mdf_pss","mdf_shb","mdf_avi","mdf_div","mdf_fnd","mdf_inb","mdf_ass","mdf_csh","mdf_gpr_q","mdf_ita_q","mdf_qty","mdf_tca","mdf_cps","mdf_dpr","mdf_tie","mdf_coa","mdf_coa_q","mdf_gry","mdf_pre","mdf_exi","mdf_oey","mdf_bsd_q","mdf_ccc_q","mdf_tas_q","mdf_atr","mdf_isd_q","mdf_nps","mdf_era","mdf_pra","mdf_yld","mdf_tli_q"]]

tipeis1 = random.choice(tipeofdata)
tipeis2 = random.choice(tipeofdata)
funda1 = tipeis1
funda2 = tipeis1
funda3 = tipeis1
funda4 = tipeis1
funda5 = tipeis1
funda6 = tipeis1
days = ["62","21","128","240","30"]
ks = ["1","2","3"]
groups = ["market","industry","sector","exchange","rank(cap)","RANK(income)/RANK(revenue)"]
operators =  ["Ts_delta","Ts_zscore","ts_skewness","ts_ir","ts_median","ts_kurtosis","ts_stddev"]


if (not funda1 or not funda2 or not funda3 or not funda4 or not funda5 or not funda6):
    
    funda1 = tipeis1
    funda2 = tipeis1
    funda3 = tipeis1
    funda4 = tipeis1
    funda5 = tipeis1
    funda6 = tipeis1
    days = ["62","21","128","240","30"]
    ks =  ["1","2","3"]
    groups = ["market","industry","sector","exchange"]
    operators =  ["Ts_delta","Ts_zscore","ts_skewness","ts_ir","ts_median","ts_kurtosis","ts_stddev"]
    techs = ["-group_neutralize(RANK(Ts_zscore(returns,62)),market)","-group_neutralize(RANK(Ts_zscore(returns,128)),market)","-group_neutralize(RANK(Ts_delta(returns,62)),market)","-group_neutralize(RANK(Ts_zscore(returns,21)),market)"]
alphas = []
for i in range(2000):
    rnddata1 = random.choice(funda1)
    rnddata2 = random.choice(funda2)
    rnddata3 = random.choice(funda3)
    rnddata4 = random.choice(funda4)
    rnddata5 = random.choice(funda5)
    rnddata6 = random.choice(funda6)
    rnddata7 = random.choice(funda5)
    rnddata8 = random.choice(funda6)
    group = random.choice(groups)
    day = random.choice(days)
    day1 = random.choice(days)
    k = random.choice(ks)
    operator = random.choice(operators)
    
    if rnddata1 == rnddata2:
        rnddata2 = random.choice(funda2)
    if rnddata4 == rnddata5:
        rnddata5 = random.choice(funda5)
    
    param1 = "(("+rnddata1+"/"+rnddata2+"))"
    param2 = "(("+rnddata4+"/"+rnddata5+"))"
    param3 = "(("+rnddata3+"/"+rnddata6+"))"
    param4 = "(("+rnddata7+"/"+rnddata8+"))"
    alpha  = "" #моя модель
    alphas.append(str(alpha))



simulate_many(client, alphas, {"region":'USA', "universe":'TOP2000', "decay":'10'})
os.system('say "End simulate"')

