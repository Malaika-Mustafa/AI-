<!DOCTYPE html>
<!-- saved from url=(0056)https://github.com/SumaikaImran/AI_LABS/blob/main/app.py -->
<html lang="en" data-color-mode="auto" data-light-theme="light" data-dark-theme="dark" data-a11y-animated-images="system" data-a11y-link-underlines="true" data-turbo-loaded="" class="js-focus-visible" data-js-focus-visible=""><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8"><style type="text/css">.turbo-progress-bar {
  position: fixed;
  display: block;
  top: 0;
  left: 0;
  height: 3px;
  background: #0076ff;
  z-index: 2147483647;
  transition:
    width 300ms ease-out,
    opacity 150ms 150ms ease-in;
  transform: translate3d(0, 0, 0);
}
</style>
    
  
  
  
  
  
  

  

  <link crossorigin="anonymous" media="all" rel="stylesheet" href="./app_files/light-3e154969b9f9.css"><link crossorigin="anonymous" media="all" rel="stylesheet" href="./app_files/dark-9c5b7a476542.css"><link data-color-theme="dark_dimmed" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/dark_dimmed-afda8eb0fb33.css"><link data-color-theme="dark_high_contrast" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/dark_high_contrast-2494e44ccdc5.css"><link data-color-theme="dark_colorblind" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/dark_colorblind-56fff47acadc.css"><link data-color-theme="light_colorblind" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/light_colorblind-71cd4cc132ec.css"><link data-color-theme="light_high_contrast" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/light_high_contrast-fd5499848985.css"><link data-color-theme="light_tritanopia" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/light_tritanopia-31d17ba3e139.css"><link data-color-theme="dark_tritanopia" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/dark_tritanopia-68d6b2c79663.css">

    <link crossorigin="anonymous" media="all" rel="stylesheet" href="./app_files/primer-primitives-4cf0d59ab51a.css">
    <link crossorigin="anonymous" media="all" rel="stylesheet" href="./app_files/primer-af846850481e.css">
    <link crossorigin="anonymous" media="all" rel="stylesheet" href="./app_files/global-8b10f05a77e6.css">
    <link crossorigin="anonymous" media="all" rel="stylesheet" href="./app_files/github-2f6e722088eb.css">
  <link crossorigin="anonymous" media="all" rel="stylesheet" href="./app_files/repository-9c77ed90200e.css">
<link crossorigin="anonymous" media="all" rel="stylesheet" href="./app_files/code-a0610fd00b47.css">

  


  <script type="application/json" id="client-env">{"locale":"en","featureFlags":["copilot_load_latest_thread","copilot_new_references_ui","copilot_beta_features_opt_in","copilot_chat_static_thread_suggestions","copilot_conversational_ux_history_refs","copilot_implicit_context","copilot_smell_icebreaker_ux","copilot_summary_beta","experimentation_azure_variant_endpoint","failbot_handle_non_errors","geojson_azure_maps","ghost_pilot_confidence_truncation_25","ghost_pilot_confidence_truncation_40","hovercard_accessibility","issues_advanced_search","issues_react_new_timeline","issues_react_avatar_refactor","issues_react_remove_placeholders","issues_react_blur_item_picker_on_close","marketing_pages_search_explore_provider","primer_react_css_modules_ga","react_keyboard_shortcuts_dialog","remove_child_patch","repository_suggester_elastic_search","sample_network_conn_type","site_metered_billing_update","issues_react_first_time_contribution_banner","lifecycle_label_name_updates","issues_react_customise_notifications_ui"],"login":"Malaika-Mustafa"}</script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./app_files/wp-runtime-6657579a8825.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./app_files/vendors-node_modules_dompurify_dist_purify_js-b73fdff77a4e.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./app_files/vendors-node_modules_oddbird_popover-polyfill_dist_popover_js-aff936e590ed.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./app_files/vendors-node_modules_github_arianotify-polyfill_ariaNotify-polyfill_js-node_modules_github_mi-247092-740e4ddd559d.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./app_files/ui_packages_failbot_failbot_ts-93b6a0551aa9.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./app_files/environment-cd35650c2e9c.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./app_files/vendors-node_modules_primer_behaviors_dist_esm_index_mjs-4aa4b0e95669.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./app_files/vendors-node_modules_github_selector-observer_dist_index_esm_js-f690fd9ae3d5.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./app_files/vendors-node_modules_github_relative-time-element_dist_index_js-6d3967acd51c.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./app_files/vendors-node_modules_github_combobox-nav_dist_index_js-node_modules_github_g-emoji-element_di-6ce195-53781cbc550f.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./app_files/vendors-node_modules_github_auto-complete-element_dist_index_js-node_modules_github_catalyst_-6afc16-3cdfa69a0406.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./app_files/vendors-node_modules_github_text-expander-element_dist_index_js-f5498b8d4e5d.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./app_files/vendors-node_modules_github_filter-input-element_dist_index_js-node_modules_github_remote-inp-b5f1d7-492b5042c841.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./app_files/vendors-node_modules_github_mini-throttle_dist_index_js-node_modules_stacktrace-parser_dist_s-1f651a-1e3d784c897c.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./app_files/vendors-node_modules_github_file-attachment-element_dist_index_js-node_modules_primer_view-co-7671f1-dc6cac136d88.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./app_files/github-elements-71486356f507.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./app_files/element-registry-e3ab8405ef80.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./app_files/vendors-node_modules_braintree_browser-detection_dist_browser-detection_js-node_modules_githu-bb80ec-634de60bacfa.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./app_files/vendors-node_modules_lit-html_lit-html_js-ce7225a304c5.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./app_files/vendors-node_modules_github_hydro-analytics-client_dist_analytics-client_js-node_modules_gith-f3aee1-e6893db9c19e.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./app_files/vendors-node_modules_github_mini-throttle_dist_index_js-node_modules_morphdom_dist_morphdom-e-7c534c-f8a5485c982a.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./app_files/vendors-node_modules_github_turbo_dist_turbo_es2017-esm_js-858e043fcf76.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./app_files/vendors-node_modules_github_remote-form_dist_index_js-node_modules_delegated-events_dist_inde-893f9f-6cf3320416b8.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./app_files/vendors-node_modules_scroll-anchoring_dist_scroll-anchoring_esm_js-node_modules_stacktrace-pa-a71630-6f3c4f0189d8.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./app_files/vendors-node_modules_color-convert_index_js-0e07cc183eed.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./app_files/vendors-node_modules_github_quote-selection_dist_index_js-node_modules_github_session-resume_-0b5e12-889cec8cf448.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./app_files/ui_packages_updatable-content_updatable-content_ts-eae9df0dd562.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./app_files/app_assets_modules_github_behaviors_task-list_ts-app_assets_modules_github_sso_ts-ui_packages-900dde-18d1c91a7872.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./app_files/app_assets_modules_github_sticky-scroll-into-view_ts-7cbef09a422c.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./app_files/app_assets_modules_github_behaviors_ajax-error_ts-app_assets_modules_github_behaviors_include-d0d0a6-0e9fa537dc4f.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./app_files/app_assets_modules_github_behaviors_commenting_edit_ts-app_assets_modules_github_behaviors_ht-83c235-c89801ebbe15.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./app_files/behaviors-a6e4c4c86bfa.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./app_files/vendors-node_modules_delegated-events_dist_index_js-node_modules_github_catalyst_lib_index_js-f6223d90c7ba.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./app_files/notifications-global-3366f6b6298e.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./app_files/vendors-node_modules_virtualized-list_es_index_js-node_modules_github_template-parts_lib_index_js-96453a51f920.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./app_files/vendors-node_modules_stacktrace-parser_dist_stack-trace-parser_esm_js-node_modules_github_bro-b0a862-4d8589138d1e.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./app_files/vendors-node_modules_github_remote-form_dist_index_js-node_modules_delegated-events_dist_inde-0e9dbe-d2bcedf65682.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./app_files/app_assets_modules_github_ref-selector_ts-043af64042a1.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./app_files/codespaces-4158520ad4d7.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./app_files/vendors-node_modules_github_mini-throttle_dist_decorators_js-node_modules_delegated-events_di-cc9bcb-ea42a360c5ae.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./app_files/vendors-node_modules_github_file-attachment-element_dist_index_js-node_modules_github_filter--35675b-aff280068839.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./app_files/repositories-ce9ff2a57e1f.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./app_files/vendors-node_modules_github_mini-throttle_dist_index_js-node_modules_github_catalyst_lib_inde-dbbea9-9b97703a4e6a.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./app_files/code-menu-13971a40799a.js.download"></script>
  
  <script crossorigin="anonymous" defer="defer" type="application/javascript" src="./app_files/primer-react-765944243383.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./app_files/react-core-cd0a67881543.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./app_files/react-lib-7b7b5264f6c1.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./app_files/octicons-react-45c3a19dd792.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./app_files/vendors-node_modules_tanstack_query-core_build_modern_queryClient_js-e40bb86d3e93.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./app_files/vendors-node_modules_emotion_is-prop-valid_dist_emotion-is-prop-valid_esm_js-node_modules_emo-37e3d5-31653d7f2342.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./app_files/vendors-node_modules_github_mini-throttle_dist_index_js-node_modules_stacktrace-parser_dist_s-e7dcdd-285fc29e9fa5.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./app_files/vendors-node_modules_oddbird_popover-polyfill_dist_popover-fn_js-4896ddd4b7bb.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./app_files/notifications-subscriptions-menu-3eda30673b32.js.download"></script>
<link crossorigin="anonymous" media="all" rel="stylesheet" href="./app_files/primer-react.9fa170e9435ed4b922b9.module.css">
<link crossorigin="anonymous" media="all" rel="stylesheet" href="./app_files/notifications-subscriptions-menu.1bcff9205c241e99cff2.module.css">


  



  
  
  

    
  


  


    


  
  

  
  

    



  

  




    

  

    

    

      

      

    
    
    

      
  
  


      
      


      


      
      
      

        


  <meta http-equiv="x-pjax-version" content="0361a11d6ba7285e98ad3340b1de5998c1adf9be672ff350e645684a12c5ff34" data-turbo-track="reload">
  <meta http-equiv="x-pjax-csp-version" content="ace39c3b6632770952207593607e6e0be0db363435a8b877b1f96abe6430f345" data-turbo-track="reload">
  <meta http-equiv="x-pjax-css-version" content="3adbaefc258174e49a9472f62ba4ed262e7c0112f9e7266a3e927bd7b898716f" data-turbo-track="reload">
  <meta http-equiv="x-pjax-js-version" content="58069173ba3ee40a605f317588f70346d3cda2c3c32d767dd6d2909bbe343612" data-turbo-track="reload">

  

      
  

  



      


    


  

  

  
  
  





  

  <style data-styled="active" data-styled-version="5.3.11"></style><style id="ms-consent-banner-main-styles">.w8hcgFksdo30C8w-bygqu{color:#000}.ydkKdaztSS0AeHWIeIHsQ a{color:#0067B8}.erL690_8JwUW-R4bJRcfl{background-color:#EBEBEB;border:none;color:#000}.erL690_8JwUW-R4bJRcfl:enabled:hover{color:#000;background-color:#DBDBDB;box-shadow:0px 4px 10px rgba(0,0,0,0.25);border:none}.erL690_8JwUW-R4bJRcfl:enabled:focus{background-color:#DBDBDB;box-shadow:0px 4px 10px rgba(0,0,0,0.25);border:2px solid #000}.erL690_8JwUW-R4bJRcfl:disabled{opacity:1;color:rgba(0,0,0,0.2);background-color:rgba(0,0,0,0.2);border:none}._1zNQOqxpBFSokeCLGi_hGr{border:none;background-color:#0067B8;color:#fff}._1zNQOqxpBFSokeCLGi_hGr:enabled:hover{color:#fff;background-color:#0067B8;box-shadow:0px 4px 10px rgba(0,0,0,0.25);border:none}._1zNQOqxpBFSokeCLGi_hGr:enabled:focus{background-color:#0067B8;box-shadow:0px 4px 10px rgba(0,0,0,0.25);border:2px solid #000}._1zNQOqxpBFSokeCLGi_hGr:disabled{opacity:1;color:rgba(0,0,0,0.2);background-color:rgba(0,120,215,0.2);border:none}._23tra1HsiiP6cT-Cka-ycB{position:relative;display:flex;z-index:9999;width:100%;background-color:#F2F2F2;justify-content:space-between;text-align:left}div[dir="rtl"]._23tra1HsiiP6cT-Cka-ycB{text-align:right}._1Upc2NjY8AlDn177YoVj0y{margin:0;padding-left:5%;padding-top:8px;padding-bottom:8px}div[dir="rtl"] ._1Upc2NjY8AlDn177YoVj0y{margin:0;padding:8px 5% 8px 0;float:none}._23tra1HsiiP6cT-Cka-ycB svg{fill:none;max-width:none;max-height:none}._1V_hlU-7jdtPiooHMu89BB{display:table-cell;padding:12px;width:24px;height:24px;font-family:Segoe UI, SegoeUI, Arial, sans-serif;font-style:normal;font-weight:normal;font-size:24px;line-height:0}.f6QKJD7fhSbnJLarTL-W-{display:table-cell;vertical-align:middle;padding:0;font-family:Segoe UI, SegoeUI, Arial, sans-serif;font-style:normal;font-weight:normal;font-size:13px;line-height:16px}.f6QKJD7fhSbnJLarTL-W- a{text-decoration:underline}._2j0fmugLb1FgYz6KPuB91w{display:inline-block;margin-left:5%;margin-right:5%;min-width:40%;min-width:calc((150px + 3 * 4px) * 2 + 150px);min-width:-webkit-fit-content;min-width:-moz-fit-content;min-width:fit-content;align-self:center;position:relative}._1XuCi2WhiqeWRUVp3pnFG3{margin:4px;padding:5px;min-width:150px;min-height:36px;vertical-align:top;cursor:pointer;font-family:Segoe UI, SegoeUI, Arial, sans-serif;font-style:normal;font-weight:normal;font-size:15px;line-height:20px;text-align:center}._1XuCi2WhiqeWRUVp3pnFG3:focus{box-sizing:border-box}._1XuCi2WhiqeWRUVp3pnFG3:disabled{cursor:not-allowed}._2bvsb3ubApyZ0UGoQA9O9T{display:block;position:fixed;z-index:10000;top:0;left:0;width:100%;height:100%;background-color:rgba(255,255,255,0.6);overflow:auto;text-align:left}div[dir="rtl"]._2bvsb3ubApyZ0UGoQA9O9T{text-align:right}div[dir="rtl"] ._2bvsb3ubApyZ0UGoQA9O9T{left:auto;right:0}.AFsJE948muYyzCMktdzuk{position:relative;top:8%;margin-bottom:40px;margin-left:auto;margin-right:auto;box-sizing:border-box;width:640px;background-color:#fff;border:1px solid #0067B8}._3kWyBRbW_dgnMiEyx06Fu4{float:right;z-index:1;margin:2px;padding:12px;border:none;cursor:pointer;font-family:Segoe UI, SegoeUI, Arial, sans-serif;font-style:normal;font-weight:normal;font-size:13px;line-height:13px;display:flex;align-items:center;text-align:center;color:#666;background-color:#fff}div[dir="rtl"] ._3kWyBRbW_dgnMiEyx06Fu4{margin:2px;padding:12px;float:left}.uCYvKvHXrhjNgflv1VqdD{position:static;margin-top:36px;margin-left:36px;margin-right:36px}._17pX1m9O_W--iZbDt3Ta5r{margin-top:0;margin-bottom:12px;font-family:Segoe UI, SegoeUI, Arial, sans-serif;font-style:normal;font-weight:600;font-size:20px;line-height:24px;text-transform:none}._1kBkHQ1V1wu3kl-YcLgUr6{height:446px;overflow:auto}._20_nXDf6uFs9Q6wxRXG-I-{margin-top:0;font-family:Segoe UI, SegoeUI, Arial, sans-serif;font-style:normal;font-weight:normal;font-size:15px;line-height:20px}._20_nXDf6uFs9Q6wxRXG-I- a{text-decoration:underline}dl._2a0NH_GDQEQe5Ynfo7suVH{margin-top:36px;margin-bottom:0;padding:0;list-style:none;text-transform:none}dt._3j_LCPv7fyXv3A8FIXVwZ4{margin-top:20px;float:none;font-family:Segoe UI, SegoeUI, Arial, sans-serif;font-style:normal;font-weight:600;font-size:18px;line-height:24px;list-style:none}.k-vxTGFbdq1aOZB2HHpjh{margin:0;padding:0;border:none}._2Bucyy75c_ogoU1g-liB5R{margin:0;padding:0;border-bottom:none;font-family:Segoe UI, SegoeUI, Arial, sans-serif;font-style:normal;font-weight:600;font-size:18px;line-height:24px;text-transform:none}._63gwfzV8dclrsl2cfd90r{display:inline-block;margin-top:0;margin-bottom:13px;font-family:Segoe UI, SegoeUI, Arial, sans-serif;font-style:normal;font-weight:normal;font-size:15px;line-height:20px}._1l8wM_4mRYGz3Iu7l3BZR7{display:block}._2UE03QS02aZGkslegN_F-i{display:inline-block;position:relative;left:5px;margin-bottom:13px;margin-right:34px;padding:3px}div[dir="rtl"] ._2UE03QS02aZGkslegN_F-i{margin:0 0 13px 34px;padding:3px;float:none}div[dir="rtl"] ._2UE03QS02aZGkslegN_F-i{left:auto;right:5px}._23tra1HsiiP6cT-Cka-ycB *::before,._2bvsb3ubApyZ0UGoQA9O9T *::before,._23tra1HsiiP6cT-Cka-ycB *::after,._2bvsb3ubApyZ0UGoQA9O9T *::after{box-sizing:inherit}._1HSFn0HzGo6w4ADApV8-c4{outline:2px solid rgba(0,0,0,0.8)}input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2{display:inline-block;position:relative;margin-top:0;margin-left:0;margin-right:0;height:0;width:0;border-radius:0;cursor:pointer;outline:none;box-sizing:border-box;-webkit-appearance:none;-moz-appearance:none;appearance:none}input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2+label::before{display:block;position:absolute;top:5px;left:3px;height:19px;width:19px;content:"";border-radius:50%;border:1px solid #000;background-color:#fff}div[dir="rtl"] input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2+label::before{left:auto;right:3px}input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2:not(:disabled)+label:hover::before{border:1px solid #0067B8}input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2:not(:disabled)+label:hover::after{display:block;position:absolute;top:10px;left:8px;height:9px;width:9px;content:"";border-radius:50%;background-color:rgba(0,0,0,0.8)}div[dir="rtl"] input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2:not(:disabled)+label:hover::after{left:auto;right:8px}input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2:not(:disabled)+label:focus::before{border:1px solid #0067B8}input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2:not(:disabled)+label:focus::after{display:block;position:absolute;top:10px;left:8px;height:9px;width:9px;content:"";border-radius:50%;background-color:#000}div[dir="rtl"] input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2:not(:disabled)+label:focus::after{left:auto;right:8px}input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2:checked+label::after{display:block;position:absolute;top:10px;left:8px;height:9px;width:9px;content:"";border-radius:50%;background-color:#000}div[dir="rtl"] input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2:checked+label::after{left:auto;right:8px}input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2:disabled+label{cursor:not-allowed}input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2:disabled+label::before{border:1px solid rgba(0,0,0,0.2);background-color:rgba(0,0,0,0.2)}._3RJzeL3l9Rl_lAQEm6VwdX{display:block;position:static;float:right;margin-top:0;margin-bottom:0;margin-left:19px;margin-right:0;padding-top:0;padding-bottom:0;padding-left:8px;padding-right:0;width:80%;width:calc(100% - 19px);font-family:Segoe UI, SegoeUI, Arial, sans-serif;font-style:normal;font-weight:normal;font-size:15px;line-height:20px;text-transform:none;cursor:pointer;box-sizing:border-box}div[dir="rtl"] ._3RJzeL3l9Rl_lAQEm6VwdX{margin:0 19px 0 0;padding:0 8px 0 0;float:left}.nohp3sIG12ZBhzcMnPala{margin-top:20px;margin-bottom:48px}._2uhaEsmeotZ3P-M0AXo2kF{padding:0;width:278px;height:36px;cursor:pointer;font-family:Segoe UI, SegoeUI, Arial, sans-serif;font-style:normal;font-weight:normal;font-size:15px;line-height:20px;text-align:center}._2uhaEsmeotZ3P-M0AXo2kF:focus{box-sizing:border-box}._2uhaEsmeotZ3P-M0AXo2kF:disabled{cursor:not-allowed}._3tOu1FJ59c_xz_PmI1lKV5{float:right;padding:0;width:278px;height:36px;cursor:pointer;font-family:Segoe UI, SegoeUI, Arial, sans-serif;font-style:normal;font-weight:normal;font-size:15px;line-height:20px;text-align:center}._3tOu1FJ59c_xz_PmI1lKV5:focus{box-sizing:border-box}._3tOu1FJ59c_xz_PmI1lKV5:disabled{cursor:not-allowed}div[dir="rtl"] ._3tOu1FJ59c_xz_PmI1lKV5{margin:0;padding:0;float:left}@media only screen and (max-width: 768px){._2j0fmugLb1FgYz6KPuB91w,._1Upc2NjY8AlDn177YoVj0y{padding-top:8px;padding-bottom:12px;padding-left:3.75%;padding-right:3.75%;margin:0;width:92.5%}._23tra1HsiiP6cT-Cka-ycB{display:block}._1XuCi2WhiqeWRUVp3pnFG3{margin-bottom:8px;margin-left:0;margin-right:0;width:100%}._2bvsb3ubApyZ0UGoQA9O9T{overflow:hidden}.AFsJE948muYyzCMktdzuk{top:1.8%;width:93.33%;height:96.4%;overflow:hidden}.uCYvKvHXrhjNgflv1VqdD{margin-top:24px;margin-left:24px;margin-right:24px;height:100%}._1kBkHQ1V1wu3kl-YcLgUr6{height:62%;height:calc(100% - 188px);min-height:50%}._2uhaEsmeotZ3P-M0AXo2kF{width:100%}._3tOu1FJ59c_xz_PmI1lKV5{margin-bottom:12px;margin-left:0;width:100%}div[dir="rtl"] ._3tOu1FJ59c_xz_PmI1lKV5{margin:0 0 12px 0;padding:0;float:none}}@media only screen and (max-width: 768px) and (orientation: landscape), only screen and (max-height: 260px), only screen and (max-width: 340px){.AFsJE948muYyzCMktdzuk{overflow:auto}}@media only screen and (max-height: 260px), only screen and (max-width: 340px){._1XuCi2WhiqeWRUVp3pnFG3{min-width:0}._3kWyBRbW_dgnMiEyx06Fu4{padding:3%}.uCYvKvHXrhjNgflv1VqdD{margin-top:3%;margin-left:3%;margin-right:3%}._17pX1m9O_W--iZbDt3Ta5r{margin-bottom:3%}._1kBkHQ1V1wu3kl-YcLgUr6{height:calc(79% - 64px)}.nohp3sIG12ZBhzcMnPala{margin-top:5%;margin-bottom:10%}._3tOu1FJ59c_xz_PmI1lKV5{margin-bottom:3%}div[dir="rtl"] ._3tOu1FJ59c_xz_PmI1lKV5{margin:0 0 3% 0;padding:0;float:none}}
</style><style type="text/css" id="ms-consent-banner-theme-styles">._23tra1HsiiP6cT-Cka-ycB {
            background-color: #24292f !important;
        }.w8hcgFksdo30C8w-bygqu {
            color: #ffffff !important;
        }.ydkKdaztSS0AeHWIeIHsQ a {
            color: #d8b9ff !important;
        }._2bvsb3ubApyZ0UGoQA9O9T {
            background-color: rgba(23, 23, 23, 0.8) !important;
        }.AFsJE948muYyzCMktdzuk {
            background-color: #24292f !important;
            border: 1px solid #d8b9ff !important;
        }._3kWyBRbW_dgnMiEyx06Fu4 {
            color: #d8b9ff !important;
            background-color: #24292f !important;
        }._1zNQOqxpBFSokeCLGi_hGr {
            border: 1px solid #ffffff !important;
            background-color: #ffffff !important;
            color: #1f2328 !important;
        }._1zNQOqxpBFSokeCLGi_hGr:enabled:hover {
            color: #1f2328 !important;
            background-color: #d8b9ff !important;
            box-shadow: none !important;
            border: 1px solid transparent !important;
        }._1zNQOqxpBFSokeCLGi_hGr:enabled:focus {
            background-color: #d8b9ff !important;
            box-shadow: none !important;
            border: 2px solid #ffffff !important;
        }._1zNQOqxpBFSokeCLGi_hGr:disabled {
            opacity: 0.5 !important;
            color: #1f2328 !important;
            background-color: #ffffff !important;
            border: 1px solid transparent !important;
        }.erL690_8JwUW-R4bJRcfl {
            border: 1px solid #eaeef2 !important;
            background-color: #32383f !important;
            color: #ffffff !important;
        }.erL690_8JwUW-R4bJRcfl:enabled:hover {
            color: #ffffff !important;
            background-color: #24292f !important;
            box-shadow: none !important;
            border: 1px solid #ffffff !important;
        }.erL690_8JwUW-R4bJRcfl:enabled:focus {
            background-color: #24292f !important;
            box-shadow: none !important;
            border: 2px solid #6e7781 !important;
        }.erL690_8JwUW-R4bJRcfl:disabled {
            opacity: 0.5 !important;
            color: #ffffff !important;
            background-color: #424a53 !important;
            border: 1px solid #6e7781 !important;
        }input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2 + label::before {
            border: 1px solid #d8b9ff !important;
            background-color: #24292f !important;
        }._1HSFn0HzGo6w4ADApV8-c4 {
            outline: 2px solid #ffffff !important;
        }input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2:checked + label::after {
            background-color: #d8b9ff !important;
        }input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2 + label:hover::before {
            border: 1px solid #ffffff !important;
        }input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2 + label:hover::after {
            background-color: #ffffff !important;
        }input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2 + label:focus::before {
            border: 1px solid #ffffff !important;
        }input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2 + label:focus::after {
            background-color: #d8b9ff !important;
        }input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2:disabled + label::before {
            border: 1px solid rgba(227, 227, 227, 0.2) !important;
            background-color: rgba(227, 227, 227, 0.2) !important;
        }</style><link crossorigin="anonymous" media="all" rel="stylesheet" href="./app_files/react-code-view.6b587a69b593e23c3657.module.css"><link crossorigin="anonymous" media="all" rel="stylesheet" href="./app_files/react-1a79343258bd.css"><script crossorigin="anonymous" defer="defer" type="application/javascript" src="./app_files/vendors-node_modules_lodash-es__Stack_js-node_modules_lodash-es__Uint8Array_js-node_modules_l-4faaa6-13a0602a5edf.js.download"></script><script crossorigin="anonymous" defer="defer" type="application/javascript" src="./app_files/vendors-node_modules_lodash-es__baseIsEqual_js-8929eb9718d5.js.download"></script><script crossorigin="anonymous" defer="defer" type="application/javascript" src="./app_files/vendors-node_modules_github_hydro-analytics-client_dist_analytics-client_js-node_modules_gith-9002b0-8e5e346f0cbe.js.download"></script><script crossorigin="anonymous" defer="defer" type="application/javascript" src="./app_files/ui_packages_aria-live_aria-live_ts-ui_packages_promise-with-resolvers-polyfill_promise-with-r-014121-e1792bd5a31e.js.download"></script><script crossorigin="anonymous" defer="defer" type="application/javascript" src="./app_files/ui_packages_paths_index_ts-c733d4a976df.js.download"></script><script crossorigin="anonymous" defer="defer" type="application/javascript" src="./app_files/ui_packages_ref-selector_RefSelector_tsx-b10086b6761e.js.download"></script><script crossorigin="anonymous" defer="defer" type="application/javascript" src="./app_files/ui_packages_code-view-shared_utilities_web-worker_ts-ui_packages_code-view-shared_worker-jobs-7fe572-d1c1cf476cef.js.download"></script><script crossorigin="anonymous" defer="defer" type="application/javascript" src="./app_files/ui_packages_hydro-analytics_hydro-analytics_ts-ui_packages_verified-fetch_verified-fetch_ts-u-4672d1-0996d093463a.js.download"></script><script crossorigin="anonymous" defer="defer" type="application/javascript" src="./app_files/ui_packages_code-view-shared_hooks_use-canonical-object_ts-ui_packages_code-view-shared_utili-228da6-37a4eeff405d.js.download"></script><script crossorigin="anonymous" defer="defer" type="application/javascript" src="./app_files/ui_packages_code-view-shared_hooks_use-file-page-payload_ts-ui_packages_code-view-shared_comp-1beb66-b07e414af699.js.download"></script><script crossorigin="anonymous" defer="defer" type="application/javascript" src="./app_files/app_assets_modules_github_blob-anchor_ts-ui_packages_code-nav_code-nav_ts-ui_packages_filter--8253c1-87c39cb5708f.js.download"></script><script crossorigin="anonymous" defer="defer" type="application/javascript" src="./app_files/react-code-view-14a709e0fc35.js.download"></script><link rel="dns-prefetch" href="https://github.githubassets.com/"><link rel="dns-prefetch" href="https://avatars.githubusercontent.com/"><link rel="dns-prefetch" href="https://github-cloud.s3.amazonaws.com/"><link rel="dns-prefetch" href="https://user-images.githubusercontent.com/"><link rel="preconnect" href="https://github.githubassets.com/" crossorigin=""><link rel="preconnect" href="https://avatars.githubusercontent.com/"><title>AI_LABS/app.py at main · SumaikaImran/AI_LABS</title><meta name="route-pattern" content="/:user_id/:repository/blob/*name(/*path)" data-turbo-transient=""><meta name="route-controller" content="blob" data-turbo-transient=""><meta name="route-action" content="show" data-turbo-transient=""><meta name="current-catalog-service-hash" content="f3abb0cc802f3d7b95fc8762b94bdcb13bf39634c40c357301c4aa1d67a256fb"><meta name="request-id" content="A2F9:362B05:23738BA:294E91E:67493A8D" data-turbo-transient="true"><meta name="html-safe-nonce" content="14da76f6f57ff82b3061f65edb490512d65ff61f84f47ce57f85ffc5c671a44f" data-turbo-transient="true"><meta name="visitor-payload" content="eyJyZWZlcnJlciI6Imh0dHBzOi8vZ2l0aHViLmNvbS9TdW1haWthSW1yYW4vQUlfTEFCUy9ibG9iL21haW4vYXBwLnB5IiwicmVxdWVzdF9pZCI6IkEyRjk6MzYyQjA1OjIzNzM4QkE6Mjk0RTkxRTo2NzQ5M0E4RCIsInZpc2l0b3JfaWQiOiI2Mzg1NTE5NTgwNjgyMTM1NDYiLCJyZWdpb25fZWRnZSI6ImNlbnRyYWxpbmRpYSIsInJlZ2lvbl9yZW5kZXIiOiJpYWQifQ==" data-turbo-transient="true"><meta name="visitor-hmac" content="4bf7fed215b4a145775615e74c25145558c3ccc5c4aa481e73184b90a6aa60d1" data-turbo-transient="true"><meta name="hovercard-subject-tag" content="repository:871997669" data-turbo-transient=""><meta name="github-keyboard-shortcuts" content="repository,source-code,file-tree,copilot" data-turbo-transient="true"><meta name="selected-link" value="repo_source" data-turbo-transient=""><link rel="assets" href="https://github.githubassets.com/"><meta name="google-site-verification" content="Apib7-x98H0j5cPqHWwSMm6dNU4GmODRoqxLiDzdx9I"><meta name="octolytics-url" content="https://collector.github.com/github/collect"><meta name="octolytics-actor-id" content="146063814"><meta name="octolytics-actor-login" content="Malaika-Mustafa"><meta name="octolytics-actor-hash" content="205e3484840b6b44ff8dca0a52f46af228474adaee742859329378a01773c8e2"><meta name="analytics-location" content="/&lt;user-name&gt;/&lt;repo-name&gt;/blob/show" data-turbo-transient="true"><meta name="user-login" content="Malaika-Mustafa"><link rel="sudo-modal" href="https://github.com/sessions/sudo_modal"><meta name="turbo-cache-control" content="no-preview" data-turbo-transient=""><meta name="turbo-cache-control" content="no-cache" data-turbo-transient=""><meta data-hydrostats="publish"><meta name="go-import" content="github.com/SumaikaImran/AI_LABS git https://github.com/SumaikaImran/AI_LABS.git"><meta name="octolytics-dimension-user_id" content="147117851"><meta name="octolytics-dimension-user_login" content="SumaikaImran"><meta name="octolytics-dimension-repository_id" content="871997669"><meta name="octolytics-dimension-repository_nwo" content="SumaikaImran/AI_LABS"><meta name="octolytics-dimension-repository_public" content="true"><meta name="octolytics-dimension-repository_is_fork" content="false"><meta name="octolytics-dimension-repository_network_root_id" content="871997669"><meta name="octolytics-dimension-repository_network_root_nwo" content="SumaikaImran/AI_LABS"><meta name="turbo-body-classes" content="logged-in env-production page-responsive"><meta name="browser-stats-url" content="https://api.github.com/_private/browser/stats"><meta name="browser-errors-url" content="https://api.github.com/_private/browser/errors"><link rel="mask-icon" href="https://github.githubassets.com/assets/pinned-octocat-093da3e6fa40.svg" color="#000000"><link rel="alternate icon" class="js-site-favicon" type="image/png" href="https://github.githubassets.com/favicons/favicon.png"><link rel="icon" class="js-site-favicon" type="image/svg+xml" href="https://github.githubassets.com/favicons/favicon.svg" data-base-href="https://github.githubassets.com/favicons/favicon"><meta name="theme-color" content="#1e2327"><meta name="color-scheme" content="light dark"><link rel="manifest" href="https://github.com/manifest.json" crossorigin="use-credentials"><style type="text/css" id="ms-consent-banner-theme-styles"></style></head>

  <body class="logged-in env-production page-responsive" style="overflow-wrap: break-word; --dialog-scrollgutter: 17px;">
    <div data-turbo-body="" class="logged-in env-production page-responsive" style="word-wrap: break-word;">
      


    <div class="position-relative header-wrapper js-header-wrapper ">
      <a href="https://github.com/SumaikaImran/AI_LABS/blob/main/app.py#start-of-content" data-skip-target-assigned="false" class="p-3 color-bg-accent-emphasis color-fg-on-emphasis show-on-focus js-skip-to-content">Skip to content</a>

      <span data-view-component="true" class="progress-pjax-loader Progress position-fixed width-full">
    <span style="width: 0%;" data-view-component="true" class="Progress-item progress-pjax-loader-bar left-0 top-0 color-bg-accent-emphasis"></span>
</span>      
      
      <script crossorigin="anonymous" defer="defer" type="application/javascript" src="./app_files/keyboard-shortcuts-dialog-f3cc184507a7.js.download"></script>
<link crossorigin="anonymous" media="all" rel="stylesheet" href="./app_files/primer-react.9fa170e9435ed4b922b9.module.css">

<react-partial partial-name="keyboard-shortcuts-dialog" data-ssr="false" data-attempted-ssr="false" data-catalyst="" class="loaded">
  
  <script type="application/json" data-target="react-partial.embeddedData">{"props":{"docsUrl":"https://docs.github.com/get-started/accessibility/keyboard-shortcuts"}}</script>
  <div data-target="react-partial.reactRoot"><div class="d-none"></div><script type="application/json" id="__PRIMER_DATA_:rp:__">{"resolvedServerColorMode":"day"}</script></div>
</react-partial>




      

          

              <header class="AppHeader" role="banner">
  <h2 class="sr-only">Navigation Menu</h2>

    

    <div class="AppHeader-globalBar pb-2 js-global-bar">
      <div class="AppHeader-globalBar-start">
          <deferred-side-panel data-url="/_side-panels/global" data-catalyst="">
  <include-fragment data-target="deferred-side-panel.fragment"><template shadowrootmode="open"><style>:host {display: block;}</style><slot></slot></template>
      <button aria-label="Open global navigation menu" data-action="click:deferred-side-panel#loadPanel click:deferred-side-panel#panelOpened" data-show-dialog-id="dialog-130e8a86-6f56-4306-bd54-891364d53ffe" id="dialog-show-dialog-130e8a86-6f56-4306-bd54-891364d53ffe" type="button" data-view-component="true" class="Button Button--iconOnly Button--secondary Button--medium AppHeader-button color-bg-transparent p-0 color-fg-muted">  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-three-bars Button-visual">
    <path d="M1 2.75A.75.75 0 0 1 1.75 2h12.5a.75.75 0 0 1 0 1.5H1.75A.75.75 0 0 1 1 2.75Zm0 5A.75.75 0 0 1 1.75 7h12.5a.75.75 0 0 1 0 1.5H1.75A.75.75 0 0 1 1 7.75ZM1.75 12h12.5a.75.75 0 0 1 0 1.5H1.75a.75.75 0 0 1 0-1.5Z"></path>
</svg>
</button>

<dialog-helper>
  <dialog data-target="deferred-side-panel.panel" id="dialog-130e8a86-6f56-4306-bd54-891364d53ffe" aria-modal="true" aria-labelledby="dialog-130e8a86-6f56-4306-bd54-891364d53ffe-title" aria-describedby="dialog-130e8a86-6f56-4306-bd54-891364d53ffe-description" data-view-component="true" class="Overlay Overlay-whenNarrow Overlay--size-small-portrait Overlay--motion-scaleFade Overlay--placement-left SidePanel Overlay--disableScroll">
    <div styles="flex-direction: row;" data-view-component="true" class="Overlay-header">
  <div class="Overlay-headerContentWrap">
    <div class="Overlay-titleWrap">
      <h1 class="Overlay-title sr-only" id="dialog-130e8a86-6f56-4306-bd54-891364d53ffe-title">
        Global navigation
      </h1>
            <div data-view-component="true" class="d-flex">
      <div data-view-component="true" class="AppHeader-logo position-relative">
        <svg aria-hidden="true" height="24" viewBox="0 0 24 24" version="1.1" width="24" data-view-component="true" class="octicon octicon-mark-github">
    <path d="M12.5.75C6.146.75 1 5.896 1 12.25c0 5.089 3.292 9.387 7.863 10.91.575.101.79-.244.79-.546 0-.273-.014-1.178-.014-2.142-2.889.532-3.636-.704-3.866-1.35-.13-.331-.69-1.352-1.18-1.625-.402-.216-.977-.748-.014-.762.906-.014 1.553.834 1.769 1.179 1.035 1.74 2.688 1.25 3.349.948.1-.747.402-1.25.733-1.538-2.559-.287-5.232-1.279-5.232-5.678 0-1.25.445-2.285 1.178-3.09-.115-.288-.517-1.467.115-3.048 0 0 .963-.302 3.163 1.179.92-.259 1.897-.388 2.875-.388.977 0 1.955.13 2.875.388 2.2-1.495 3.162-1.179 3.162-1.179.633 1.581.23 2.76.115 3.048.733.805 1.179 1.825 1.179 3.09 0 4.413-2.688 5.39-5.247 5.678.417.36.776 1.05.776 2.128 0 1.538-.014 2.774-.014 3.162 0 .302.216.662.79.547C20.709 21.637 24 17.324 24 12.25 24 5.896 18.854.75 12.5.75Z"></path>
</svg>
</div></div>
    </div>
    <div class="Overlay-actionWrap">
      <button data-close-dialog-id="dialog-130e8a86-6f56-4306-bd54-891364d53ffe" aria-label="Close" type="button" data-view-component="true" class="close-button Overlay-closeButton"><svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-x">
    <path d="M3.72 3.72a.75.75 0 0 1 1.06 0L8 6.94l3.22-3.22a.749.749 0 0 1 1.275.326.749.749 0 0 1-.215.734L9.06 8l3.22 3.22a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L8 9.06l-3.22 3.22a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042L6.94 8 3.72 4.78a.75.75 0 0 1 0-1.06Z"></path>
</svg></button>
    </div>
  </div>
  
</div>
      <scrollable-region data-labelled-by="dialog-130e8a86-6f56-4306-bd54-891364d53ffe-title" data-catalyst="" style="overflow: auto;">
        <div data-view-component="true" class="Overlay-body d-flex flex-column px-2">    <div data-view-component="true" class="d-flex flex-column mb-3">
        <nav aria-label="Site navigation" data-view-component="true" class="ActionList">
  
  <nav-list data-catalyst="">
    <ul data-target="nav-list.topLevelList" data-view-component="true" class="ActionListWrap">
        
          
<li data-item-id="" data-targets="nav-list.items" data-view-component="true" class="ActionListItem">
    
    
    <a data-hotkey="g d" data-analytics-event="{&quot;category&quot;:&quot;Global navigation&quot;,&quot;action&quot;:&quot;HOME&quot;,&quot;label&quot;:null}" id="item-a7e38123-ddfd-424d-bb23-f52caf4d2534" href="https://github.com/dashboard" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-home">
    <path d="M6.906.664a1.749 1.749 0 0 1 2.187 0l5.25 4.2c.415.332.657.835.657 1.367v7.019A1.75 1.75 0 0 1 13.25 15h-3.5a.75.75 0 0 1-.75-.75V9H7v5.25a.75.75 0 0 1-.75.75h-3.5A1.75 1.75 0 0 1 1 13.25V6.23c0-.531.242-1.034.657-1.366l5.25-4.2Zm1.25 1.171a.25.25 0 0 0-.312 0l-5.25 4.2a.25.25 0 0 0-.094.196v7.019c0 .138.112.25.25.25H5.5V8.25a.75.75 0 0 1 .75-.75h3.5a.75.75 0 0 1 .75.75v5.25h2.75a.25.25 0 0 0 .25-.25V6.23a.25.25 0 0 0-.094-.195Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Home
</span>      
</a>
  
</li>

        
          
<li data-item-id="" data-targets="nav-list.items" data-view-component="true" class="ActionListItem">
    
    
    <a data-hotkey="g i" data-analytics-event="{&quot;category&quot;:&quot;Global navigation&quot;,&quot;action&quot;:&quot;ISSUES&quot;,&quot;label&quot;:null}" id="item-da716d6d-1b9d-4096-a668-9331172068df" href="https://github.com/issues" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-issue-opened">
    <path d="M8 9.5a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Z"></path><path d="M8 0a8 8 0 1 1 0 16A8 8 0 0 1 8 0ZM1.5 8a6.5 6.5 0 1 0 13 0 6.5 6.5 0 0 0-13 0Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Issues
</span>      
</a>
  
</li>

        
          
<li data-item-id="" data-targets="nav-list.items" data-view-component="true" class="ActionListItem">
    
    
    <a data-hotkey="g p" data-analytics-event="{&quot;category&quot;:&quot;Global navigation&quot;,&quot;action&quot;:&quot;PULL_REQUESTS&quot;,&quot;label&quot;:null}" id="item-a0d1a08b-f072-4b22-bad8-026c5152c404" href="https://github.com/pulls" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-git-pull-request">
    <path d="M1.5 3.25a2.25 2.25 0 1 1 3 2.122v5.256a2.251 2.251 0 1 1-1.5 0V5.372A2.25 2.25 0 0 1 1.5 3.25Zm5.677-.177L9.573.677A.25.25 0 0 1 10 .854V2.5h1A2.5 2.5 0 0 1 13.5 5v5.628a2.251 2.251 0 1 1-1.5 0V5a1 1 0 0 0-1-1h-1v1.646a.25.25 0 0 1-.427.177L7.177 3.427a.25.25 0 0 1 0-.354ZM3.75 2.5a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5Zm0 9.5a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5Zm8.25.75a.75.75 0 1 0 1.5 0 .75.75 0 0 0-1.5 0Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Pull requests
</span>      
</a>
  
</li>

        
          
<li data-item-id="" data-targets="nav-list.items" data-view-component="true" class="ActionListItem">
    
    
    <a data-analytics-event="{&quot;category&quot;:&quot;Global navigation&quot;,&quot;action&quot;:&quot;PROJECTS&quot;,&quot;label&quot;:null}" id="item-5a79be5d-04dd-4c75-a806-2a7194a369d3" href="https://github.com/projects" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-table">
    <path d="M0 1.75C0 .784.784 0 1.75 0h12.5C15.216 0 16 .784 16 1.75v12.5A1.75 1.75 0 0 1 14.25 16H1.75A1.75 1.75 0 0 1 0 14.25ZM6.5 6.5v8h7.75a.25.25 0 0 0 .25-.25V6.5Zm8-1.5V1.75a.25.25 0 0 0-.25-.25H6.5V5Zm-13 1.5v7.75c0 .138.112.25.25.25H5v-8ZM5 5V1.5H1.75a.25.25 0 0 0-.25.25V5Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Projects
</span>      
</a>
  
</li>

        
          
<li data-item-id="" data-targets="nav-list.items" data-view-component="true" class="ActionListItem">
    
    
    <a data-analytics-event="{&quot;category&quot;:&quot;Global navigation&quot;,&quot;action&quot;:&quot;DISCUSSIONS&quot;,&quot;label&quot;:null}" id="item-c070cfb6-0dfa-4e16-bd91-92a97771a1f3" href="https://github.com/discussions" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-comment-discussion">
    <path d="M1.75 1h8.5c.966 0 1.75.784 1.75 1.75v5.5A1.75 1.75 0 0 1 10.25 10H7.061l-2.574 2.573A1.458 1.458 0 0 1 2 11.543V10h-.25A1.75 1.75 0 0 1 0 8.25v-5.5C0 1.784.784 1 1.75 1ZM1.5 2.75v5.5c0 .138.112.25.25.25h1a.75.75 0 0 1 .75.75v2.19l2.72-2.72a.749.749 0 0 1 .53-.22h3.5a.25.25 0 0 0 .25-.25v-5.5a.25.25 0 0 0-.25-.25h-8.5a.25.25 0 0 0-.25.25Zm13 2a.25.25 0 0 0-.25-.25h-.5a.75.75 0 0 1 0-1.5h.5c.966 0 1.75.784 1.75 1.75v5.5A1.75 1.75 0 0 1 14.25 12H14v1.543a1.458 1.458 0 0 1-2.487 1.03L9.22 12.28a.749.749 0 0 1 .326-1.275.749.749 0 0 1 .734.215l2.22 2.22v-2.19a.75.75 0 0 1 .75-.75h1a.25.25 0 0 0 .25-.25Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Discussions
</span>      
</a>
  
</li>

        
          
<li data-item-id="" data-targets="nav-list.items" data-view-component="true" class="ActionListItem">
    
    
    <a data-analytics-event="{&quot;category&quot;:&quot;Global navigation&quot;,&quot;action&quot;:&quot;CODESPACES&quot;,&quot;label&quot;:null}" id="item-b87ab034-7c44-4b2f-a322-cc63dde24358" href="https://github.com/codespaces" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-codespaces">
    <path d="M0 11.25c0-.966.784-1.75 1.75-1.75h12.5c.966 0 1.75.784 1.75 1.75v3A1.75 1.75 0 0 1 14.25 16H1.75A1.75 1.75 0 0 1 0 14.25Zm2-9.5C2 .784 2.784 0 3.75 0h8.5C13.216 0 14 .784 14 1.75v5a1.75 1.75 0 0 1-1.75 1.75h-8.5A1.75 1.75 0 0 1 2 6.75Zm1.75-.25a.25.25 0 0 0-.25.25v5c0 .138.112.25.25.25h8.5a.25.25 0 0 0 .25-.25v-5a.25.25 0 0 0-.25-.25Zm-2 9.5a.25.25 0 0 0-.25.25v3c0 .138.112.25.25.25h12.5a.25.25 0 0 0 .25-.25v-3a.25.25 0 0 0-.25-.25Z"></path><path d="M7 12.75a.75.75 0 0 1 .75-.75h4.5a.75.75 0 0 1 0 1.5h-4.5a.75.75 0 0 1-.75-.75Zm-4 0a.75.75 0 0 1 .75-.75h.5a.75.75 0 0 1 0 1.5h-.5a.75.75 0 0 1-.75-.75Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Codespaces
</span>      
</a>
  
</li>

        
          <li role="presentation" aria-hidden="true" data-view-component="true" class="ActionList-sectionDivider"></li>
        
          
<li data-item-id="" data-targets="nav-list.items" data-view-component="true" class="ActionListItem">
    
    
    <a data-analytics-event="{&quot;category&quot;:&quot;Global navigation&quot;,&quot;action&quot;:&quot;EXPLORE&quot;,&quot;label&quot;:null}" id="item-c7b3e417-6a50-4410-8693-98e921a36ca8" href="https://github.com/explore" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-telescope">
    <path d="M14.184 1.143v-.001l1.422 2.464a1.75 1.75 0 0 1-.757 2.451L3.104 11.713a1.75 1.75 0 0 1-2.275-.702l-.447-.775a1.75 1.75 0 0 1 .53-2.32L11.682.573a1.748 1.748 0 0 1 2.502.57Zm-4.709 9.32h-.001l2.644 3.863a.75.75 0 1 1-1.238.848l-1.881-2.75v2.826a.75.75 0 0 1-1.5 0v-2.826l-1.881 2.75a.75.75 0 1 1-1.238-.848l2.049-2.992a.746.746 0 0 1 .293-.253l1.809-.87a.749.749 0 0 1 .944.252ZM9.436 3.92h-.001l-4.97 3.39.942 1.63 5.42-2.61Zm3.091-2.108h.001l-1.85 1.26 1.505 2.605 2.016-.97a.247.247 0 0 0 .13-.151.247.247 0 0 0-.022-.199l-1.422-2.464a.253.253 0 0 0-.161-.119.254.254 0 0 0-.197.038ZM1.756 9.157a.25.25 0 0 0-.075.33l.447.775a.25.25 0 0 0 .325.1l1.598-.769-.83-1.436-1.465 1Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Explore
</span>      
</a>
  
</li>

        
          
<li data-item-id="" data-targets="nav-list.items" data-view-component="true" class="ActionListItem">
    
    
    <a data-analytics-event="{&quot;category&quot;:&quot;Global navigation&quot;,&quot;action&quot;:&quot;MARKETPLACE&quot;,&quot;label&quot;:null}" id="item-dc7afc8c-ddac-4bb1-a8e0-791f7f4f359c" href="https://github.com/marketplace" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-gift">
    <path d="M2 2.75A2.75 2.75 0 0 1 4.75 0c.983 0 1.873.42 2.57 1.232.268.318.497.668.68 1.042.183-.375.411-.725.68-1.044C9.376.42 10.266 0 11.25 0a2.75 2.75 0 0 1 2.45 4h.55c.966 0 1.75.784 1.75 1.75v2c0 .698-.409 1.301-1 1.582v4.918A1.75 1.75 0 0 1 13.25 16H2.75A1.75 1.75 0 0 1 1 14.25V9.332C.409 9.05 0 8.448 0 7.75v-2C0 4.784.784 4 1.75 4h.55c-.192-.375-.3-.8-.3-1.25ZM7.25 9.5H2.5v4.75c0 .138.112.25.25.25h4.5Zm1.5 0v5h4.5a.25.25 0 0 0 .25-.25V9.5Zm0-4V8h5.5a.25.25 0 0 0 .25-.25v-2a.25.25 0 0 0-.25-.25Zm-7 0a.25.25 0 0 0-.25.25v2c0 .138.112.25.25.25h5.5V5.5h-5.5Zm3-4a1.25 1.25 0 0 0 0 2.5h2.309c-.233-.818-.542-1.401-.878-1.793-.43-.502-.915-.707-1.431-.707ZM8.941 4h2.309a1.25 1.25 0 0 0 0-2.5c-.516 0-1 .205-1.43.707-.337.392-.646.975-.879 1.793Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Marketplace
</span>      
</a>
  
</li>

</ul>  </nav-list>
</nav>

        <div data-view-component="true" class="my-3 d-flex flex-justify-center height-full">
          <span data-view-component="true">
  <svg style="box-sizing: content-box; color: var(--color-icon-primary);" width="16" height="16" viewBox="0 0 16 16" fill="none" aria-hidden="true" data-view-component="true" class="anim-rotate">
    <circle cx="8" cy="8" r="7" stroke="currentColor" stroke-opacity="0.25" stroke-width="2" vector-effect="non-scaling-stroke" fill="none"></circle>
    <path d="M15 8a7.002 7.002 0 00-7-7" stroke="currentColor" stroke-width="2" stroke-linecap="round" vector-effect="non-scaling-stroke"></path>
</svg>    <span class="sr-only">Loading</span>
</span>
</div>
</div>
      <div data-view-component="true" class="flex-1"></div>


      <div data-view-component="true" class="px-2">      <p class="color-fg-subtle text-small text-light">© 2024 GitHub, Inc.</p>

      <div data-view-component="true" class="d-flex flex-wrap text-small text-light">
          <a target="_blank" href="https://github.com/about" data-view-component="true" class="Link mr-2">About</a>
          <a target="_blank" href="https://github.blog/" data-view-component="true" class="Link mr-2">Blog</a>
          <a target="_blank" href="https://docs.github.com/site-policy/github-terms/github-terms-of-service" data-view-component="true" class="Link mr-2">Terms</a>
          <a target="_blank" href="https://docs.github.com/site-policy/privacy-policies/github-privacy-statement" data-view-component="true" class="Link mr-2">Privacy</a>
          <a target="_blank" href="https://github.com/security" data-view-component="true" class="Link mr-2">Security</a>
          <a target="_blank" href="https://www.githubstatus.com/" data-view-component="true" class="Link mr-3">Status</a>

</div></div>
</div>
      </scrollable-region>
      
</dialog></dialog-helper>

  </include-fragment>
</deferred-side-panel>

        <a class="AppHeader-logo ml-2" href="https://github.com/" data-hotkey="g d" aria-label="Homepage " data-turbo="false" data-analytics-event="{&quot;category&quot;:&quot;Header&quot;,&quot;action&quot;:&quot;go to dashboard&quot;,&quot;label&quot;:&quot;icon:logo&quot;}">
          <svg height="32" aria-hidden="true" viewBox="0 0 24 24" version="1.1" width="32" data-view-component="true" class="octicon octicon-mark-github v-align-middle color-fg-default">
    <path d="M12.5.75C6.146.75 1 5.896 1 12.25c0 5.089 3.292 9.387 7.863 10.91.575.101.79-.244.79-.546 0-.273-.014-1.178-.014-2.142-2.889.532-3.636-.704-3.866-1.35-.13-.331-.69-1.352-1.18-1.625-.402-.216-.977-.748-.014-.762.906-.014 1.553.834 1.769 1.179 1.035 1.74 2.688 1.25 3.349.948.1-.747.402-1.25.733-1.538-2.559-.287-5.232-1.279-5.232-5.678 0-1.25.445-2.285 1.178-3.09-.115-.288-.517-1.467.115-3.048 0 0 .963-.302 3.163 1.179.92-.259 1.897-.388 2.875-.388.977 0 1.955.13 2.875.388 2.2-1.495 3.162-1.179 3.162-1.179.633 1.581.23 2.76.115 3.048.733.805 1.179 1.825 1.179 3.09 0 4.413-2.688 5.39-5.247 5.678.417.36.776 1.05.776 2.128 0 1.538-.014 2.774-.014 3.162 0 .302.216.662.79.547C20.709 21.637 24 17.324 24 12.25 24 5.896 18.854.75 12.5.75Z"></path>
</svg>
        </a>

          <div class="AppHeader-context">
  <div class="AppHeader-context-compact">
      <button aria-expanded="false" aria-haspopup="dialog" aria-label="Page context: SumaikaImran / AI_LABS" id="dialog-show-context-region-dialog" data-show-dialog-id="context-region-dialog" type="button" data-view-component="true" class="AppHeader-context-compact-trigger Truncate Button--secondary Button--medium Button box-shadow-none">  <span class="Button-content">
    <span class="Button-label"><span class="AppHeader-context-compact-lead">
                <span class="AppHeader-context-compact-parentItem">SumaikaImran</span>
                <span class="no-wrap">&nbsp;/</span>

            </span>

            <strong class="AppHeader-context-compact-mainItem d-flex flex-items-center Truncate">
  <span class="Truncate-text ">AI_LABS</span>

</strong></span>
  </span>
</button>

<dialog-helper>
  <dialog id="context-region-dialog" aria-modal="true" aria-labelledby="context-region-dialog-title" aria-describedby="context-region-dialog-description" data-view-component="true" class="Overlay Overlay-whenNarrow Overlay--size-medium Overlay--motion-scaleFade Overlay--disableScroll">
    <div data-view-component="true" class="Overlay-header">
  <div class="Overlay-headerContentWrap">
    <div class="Overlay-titleWrap">
      <h1 class="Overlay-title " id="context-region-dialog-title">
        Navigate back to
      </h1>
        
    </div>
    <div class="Overlay-actionWrap">
      <button data-close-dialog-id="context-region-dialog" aria-label="Close" type="button" data-view-component="true" class="close-button Overlay-closeButton"><svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-x">
    <path d="M3.72 3.72a.75.75 0 0 1 1.06 0L8 6.94l3.22-3.22a.749.749 0 0 1 1.275.326.749.749 0 0 1-.215.734L9.06 8l3.22 3.22a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L8 9.06l-3.22 3.22a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042L6.94 8 3.72 4.78a.75.75 0 0 1 0-1.06Z"></path>
</svg></button>
    </div>
  </div>
  
</div>
      <scrollable-region data-labelled-by="context-region-dialog-title" data-catalyst="" style="overflow: auto;">
        <div data-view-component="true" class="Overlay-body">          <ul role="list" class="list-style-none">
    <li>
      <a data-analytics-event="{&quot;category&quot;:&quot;SiteHeaderComponent&quot;,&quot;action&quot;:&quot;context_region_crumb&quot;,&quot;label&quot;:&quot;SumaikaImran&quot;,&quot;screen_size&quot;:&quot;compact&quot;}" href="https://github.com/SumaikaImran" data-view-component="true" class="Link--primary Truncate d-flex flex-items-center py-1">
        <span class="AppHeader-context-item-label Truncate-text ">
            <svg aria-hidden="true" height="12" viewBox="0 0 16 16" version="1.1" width="12" data-view-component="true" class="octicon octicon-person mr-1">
    <path d="M10.561 8.073a6.005 6.005 0 0 1 3.432 5.142.75.75 0 1 1-1.498.07 4.5 4.5 0 0 0-8.99 0 .75.75 0 0 1-1.498-.07 6.004 6.004 0 0 1 3.431-5.142 3.999 3.999 0 1 1 5.123 0ZM10.5 5a2.5 2.5 0 1 0-5 0 2.5 2.5 0 0 0 5 0Z"></path>
</svg>

          SumaikaImran
        </span>

</a>
    </li>
    <li>
      <a data-analytics-event="{&quot;category&quot;:&quot;SiteHeaderComponent&quot;,&quot;action&quot;:&quot;context_region_crumb&quot;,&quot;label&quot;:&quot;AI_LABS&quot;,&quot;screen_size&quot;:&quot;compact&quot;}" href="https://github.com/SumaikaImran/AI_LABS" data-view-component="true" class="Link--primary Truncate d-flex flex-items-center py-1">
        <span class="AppHeader-context-item-label Truncate-text ">
            <svg aria-hidden="true" height="12" viewBox="0 0 16 16" version="1.1" width="12" data-view-component="true" class="octicon octicon-repo mr-1">
    <path d="M2 2.5A2.5 2.5 0 0 1 4.5 0h8.75a.75.75 0 0 1 .75.75v12.5a.75.75 0 0 1-.75.75h-2.5a.75.75 0 0 1 0-1.5h1.75v-2h-8a1 1 0 0 0-.714 1.7.75.75 0 1 1-1.072 1.05A2.495 2.495 0 0 1 2 11.5Zm10.5-1h-8a1 1 0 0 0-1 1v6.708A2.486 2.486 0 0 1 4.5 9h8ZM5 12.25a.25.25 0 0 1 .25-.25h3.5a.25.25 0 0 1 .25.25v3.25a.25.25 0 0 1-.4.2l-1.45-1.087a.249.249 0 0 0-.3 0L5.4 15.7a.25.25 0 0 1-.4-.2Z"></path>
</svg>

          AI_LABS
        </span>

</a>
    </li>
</ul>

</div>
      </scrollable-region>
      
</dialog></dialog-helper>
  </div>

  <div class="AppHeader-context-full">
    <nav role="navigation" aria-label="Page context">
      <ul role="list" class="list-style-none">
    <li>
      <a data-analytics-event="{&quot;category&quot;:&quot;SiteHeaderComponent&quot;,&quot;action&quot;:&quot;context_region_crumb&quot;,&quot;label&quot;:&quot;SumaikaImran&quot;,&quot;screen_size&quot;:&quot;full&quot;}" data-hovercard-type="user" data-hovercard-url="/users/SumaikaImran/hovercard" data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/SumaikaImran" data-view-component="true" class="AppHeader-context-item">
        <span class="AppHeader-context-item-label  ">

          SumaikaImran
        </span>

</a>
        <span class="AppHeader-context-item-separator">/</span>
    </li>
    <li>
      <a data-analytics-event="{&quot;category&quot;:&quot;SiteHeaderComponent&quot;,&quot;action&quot;:&quot;context_region_crumb&quot;,&quot;label&quot;:&quot;AI_LABS&quot;,&quot;screen_size&quot;:&quot;full&quot;}" href="https://github.com/SumaikaImran/AI_LABS" data-view-component="true" class="AppHeader-context-item">
        <span class="AppHeader-context-item-label  ">

          AI_LABS
        </span>

</a>
    </li>
</ul>

    </nav>
  </div>
</div>

      </div>
      <div class="AppHeader-globalBar-end">
          <div class="AppHeader-search">
              


<qbsearch-input class="search-input" data-scope="repo:SumaikaImran/AI_LABS" data-custom-scopes-path="/search/custom_scopes" data-delete-custom-scopes-csrf="_VqxtYLehFQdEgz12Lb1RTcZnhqSlLJQvOffJuihiCVkE_fqRtxm6ckcS0wO8N1a1qNnCw7I5_cR3ki1QGZ7sQ" data-max-custom-scopes="10" data-header-redesign-enabled="true" data-initial-value="" data-blackbird-suggestions-path="/search/suggestions" data-jump-to-suggestions-path="/_graphql/GetSuggestedNavigationDestinations" data-current-repository="SumaikaImran/AI_LABS" data-current-org="" data-current-owner="SumaikaImran" data-logged-in="true" data-copilot-chat-enabled="false" data-nl-search-enabled="false" data-catalyst="">
  <div class="search-input-container search-with-dialog position-relative d-flex flex-row flex-items-center height-auto color-bg-transparent border-0 color-fg-subtle mx-0" data-action="click:qbsearch-input#searchInputContainerClicked">
      
            <button type="button" data-action="click:qbsearch-input#handleExpand" class="AppHeader-button AppHeader-search-whenNarrow" aria-label="Search or jump to…" aria-expanded="false" aria-haspopup="dialog">
            <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-search">
    <path d="M10.68 11.74a6 6 0 0 1-7.922-8.982 6 6 0 0 1 8.982 7.922l3.04 3.04a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215ZM11.5 7a4.499 4.499 0 1 0-8.997 0A4.499 4.499 0 0 0 11.5 7Z"></path>
</svg>
          </button>


<div class="AppHeader-search-whenRegular">
  <div class="AppHeader-search-wrap AppHeader-search-wrap--hasTrailing">
    <div class="AppHeader-search-control">
      <label for="AppHeader-searchInput" aria-label="Search or jump to…" class="AppHeader-search-visual--leading">
        <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-search">
    <path d="M10.68 11.74a6 6 0 0 1-7.922-8.982 6 6 0 0 1 8.982 7.922l3.04 3.04a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215ZM11.5 7a4.499 4.499 0 1 0-8.997 0A4.499 4.499 0 0 0 11.5 7Z"></path>
</svg>
      </label>

                <button type="button" data-target="qbsearch-input.inputButton" data-action="click:qbsearch-input#handleExpand" class="AppHeader-searchButton form-control input-contrast text-left color-fg-subtle no-wrap placeholder" data-hotkey="s,/" data-analytics-event="{&quot;location&quot;:&quot;navbar&quot;,&quot;action&quot;:&quot;searchbar&quot;,&quot;context&quot;:&quot;global&quot;,&quot;tag&quot;:&quot;input&quot;,&quot;label&quot;:&quot;searchbar_input_global_navbar&quot;}" aria-describedby="search-error-message-flash">
            <div class="overflow-hidden">
              <span id="qb-input-query" data-target="qbsearch-input.inputButtonText">
                  Type <kbd class="AppHeader-search-kbd">/</kbd> to search
              </span>
            </div>
          </button>

    </div>


  </div>
</div>

    <input type="hidden" name="type" class="js-site-search-type-field">

    
<div class="Overlay--hidden " data-modal-dialog-overlay="">
  <modal-dialog data-action="close:qbsearch-input#handleClose cancel:qbsearch-input#handleClose" data-target="qbsearch-input.searchSuggestionsDialog" role="dialog" id="search-suggestions-dialog" aria-modal="true" aria-labelledby="search-suggestions-dialog-header" data-view-component="true" class="Overlay Overlay--width-medium Overlay--height-auto">
      <h1 id="search-suggestions-dialog-header" class="sr-only">Search code, repositories, users, issues, pull requests...</h1>
    <div class="Overlay-body Overlay-body--paddingNone">
      
          <div data-view-component="true">        <div class="search-suggestions position-absolute width-full color-shadow-large border color-fg-default color-bg-default overflow-hidden d-flex flex-column query-builder-container" style="border-radius: 12px;" data-target="qbsearch-input.queryBuilderContainer" hidden="">
          <!-- '"` --><!-- </textarea></xmp> --><form id="query-builder-test-form" action="https://github.com/SumaikaImran/AI_LABS/blob/main/app.py" accept-charset="UTF-8" method="get">
  <query-builder data-target="qbsearch-input.queryBuilder" id="query-builder-query-builder-test" data-filter-key=":" data-view-component="true" class="QueryBuilder search-query-builder" data-min-width="300" data-catalyst="">
    <div class="FormControl FormControl--fullWidth">
      <label id="query-builder-test-label" for="query-builder-test" class="FormControl-label sr-only">
        Search
      </label>
      <div class="QueryBuilder-StyledInput width-fit " data-target="query-builder.styledInput">
          <span id="query-builder-test-leadingvisual-wrap" class="FormControl-input-leadingVisualWrap QueryBuilder-leadingVisualWrap">
            <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-search FormControl-input-leadingVisual">
    <path d="M10.68 11.74a6 6 0 0 1-7.922-8.982 6 6 0 0 1 8.982 7.922l3.04 3.04a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215ZM11.5 7a4.499 4.499 0 1 0-8.997 0A4.499 4.499 0 0 0 11.5 7Z"></path>
</svg>
          </span>
        <div data-target="query-builder.styledInputContainer" class="QueryBuilder-StyledInputContainer">
          <div aria-hidden="true" class="QueryBuilder-StyledInputContent" data-target="query-builder.styledInputContent"></div>
          <div class="QueryBuilder-InputWrapper">
            <div aria-hidden="true" class="QueryBuilder-Sizer" data-target="query-builder.sizer"><span></span></div>
            <input id="query-builder-test" name="query-builder-test" value="" autocomplete="off" type="text" role="combobox" spellcheck="false" aria-expanded="false" aria-describedby="validation-8f80fdd8-ab9a-4064-be5c-0e58e8850bdb" data-target="query-builder.input" data-action="
          input:query-builder#inputChange
          blur:query-builder#inputBlur
          keydown:query-builder#inputKeydown
          focus:query-builder#inputFocus
        " data-view-component="true" class="FormControl-input QueryBuilder-Input FormControl-medium" aria-controls="query-builder-test-results" aria-autocomplete="list" aria-haspopup="listbox" style="width: 300px;">
          </div>
        </div>
          <span class="sr-only" id="query-builder-test-clear">Clear</span>
          <button role="button" id="query-builder-test-clear-button" aria-labelledby="query-builder-test-clear query-builder-test-label" data-target="query-builder.clearButton" data-action="
                click:query-builder#clear
                focus:query-builder#clearButtonFocus
                blur:query-builder#clearButtonBlur
              " variant="small" hidden="" type="button" data-view-component="true" class="Button Button--iconOnly Button--invisible Button--medium mr-1 px-2 py-0 d-flex flex-items-center rounded-1 color-fg-muted">  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-x-circle-fill Button-visual">
    <path d="M2.343 13.657A8 8 0 1 1 13.658 2.343 8 8 0 0 1 2.343 13.657ZM6.03 4.97a.751.751 0 0 0-1.042.018.751.751 0 0 0-.018 1.042L6.94 8 4.97 9.97a.749.749 0 0 0 .326 1.275.749.749 0 0 0 .734-.215L8 9.06l1.97 1.97a.749.749 0 0 0 1.275-.326.749.749 0 0 0-.215-.734L9.06 8l1.97-1.97a.749.749 0 0 0-.326-1.275.749.749 0 0 0-.734.215L8 6.94Z"></path>
</svg>
</button>

      </div>
      <template id="search-icon"></template>

<template id="code-icon"></template>

<template id="file-code-icon"></template>

<template id="history-icon"></template>

<template id="repo-icon"></template>

<template id="bookmark-icon"></template>

<template id="plus-circle-icon"></template>

<template id="circle-icon"></template>

<template id="trash-icon"></template>

<template id="team-icon"></template>

<template id="project-icon"></template>

<template id="pencil-icon"></template>

<template id="copilot-icon"></template>

<template id="copilot-error-icon"></template>

<template id="workflow-icon"></template>

<template id="book-icon"></template>

<template id="code-review-icon"></template>

<template id="codespaces-icon"></template>

<template id="comment-icon"></template>

<template id="comment-discussion-icon"></template>

<template id="organization-icon"></template>

<template id="rocket-icon"></template>

<template id="shield-check-icon"></template>

<template id="heart-icon"></template>

<template id="server-icon"></template>

<template id="globe-icon"></template>

<template id="issue-opened-icon"></template>

<template id="device-mobile-icon"></template>

<template id="package-icon"></template>

<template id="credit-card-icon"></template>

<template id="play-icon"></template>

<template id="gift-icon"></template>

<template id="code-square-icon"></template>

<template id="device-desktop-icon"></template>

        <div class="position-relative">
                <ul role="listbox" class="ActionListWrap QueryBuilder-ListWrap" aria-label="Suggestions" data-action="
                    combobox-commit:query-builder#comboboxCommit
                    mousedown:query-builder#resultsMousedown
                  " data-target="query-builder.resultsList" data-persist-list="false" id="query-builder-test-results"></ul>
        </div>
      <div class="FormControl-inlineValidation" id="validation-8f80fdd8-ab9a-4064-be5c-0e58e8850bdb" hidden="hidden">
        <span class="FormControl-inlineValidation--visual">
          <svg aria-hidden="true" height="12" viewBox="0 0 12 12" version="1.1" width="12" data-view-component="true" class="octicon octicon-alert-fill">
    <path d="M4.855.708c.5-.896 1.79-.896 2.29 0l4.675 8.351a1.312 1.312 0 0 1-1.146 1.954H1.33A1.313 1.313 0 0 1 .183 9.058ZM7 7V3H5v4Zm-1 3a1 1 0 1 0 0-2 1 1 0 0 0 0 2Z"></path>
</svg>
        </span>
        <span></span>
</div>    </div>
    <div data-target="query-builder.screenReaderFeedback" aria-live="polite" aria-atomic="true" class="sr-only">0 suggestions.</div>
</query-builder></form>
          <div class="d-flex flex-row color-fg-muted px-3 text-small color-bg-default search-feedback-prompt">
            <a target="_blank" href="https://docs.github.com/search-github/github-code-search/understanding-github-code-search-syntax" data-view-component="true" class="Link color-fg-accent text-normal ml-2">
              Search syntax tips
</a>            <div class="d-flex flex-1"></div>
              <button data-action="click:qbsearch-input#showFeedbackDialog" type="button" data-view-component="true" class="Button--link Button--medium Button color-fg-accent text-normal ml-2">  <span class="Button-content">
    <span class="Button-label">Give feedback</span>
  </span>
</button>
          </div>
        </div>
</div>

    </div>
</modal-dialog></div>
  </div>
  <div data-action="click:qbsearch-input#retract" class="dark-backdrop position-fixed" hidden="" data-target="qbsearch-input.darkBackdrop"></div>
  <div class="color-fg-default">
    
<dialog-helper>
  <dialog data-target="qbsearch-input.feedbackDialog" data-action="close:qbsearch-input#handleDialogClose cancel:qbsearch-input#handleDialogClose" id="feedback-dialog" aria-modal="true" aria-labelledby="feedback-dialog-title" aria-describedby="feedback-dialog-description" data-view-component="true" class="Overlay Overlay-whenNarrow Overlay--size-medium Overlay--motion-scaleFade Overlay--disableScroll">
    <div data-view-component="true" class="Overlay-header">
  <div class="Overlay-headerContentWrap">
    <div class="Overlay-titleWrap">
      <h1 class="Overlay-title " id="feedback-dialog-title">
        Provide feedback
      </h1>
        
    </div>
    <div class="Overlay-actionWrap">
      <button data-close-dialog-id="feedback-dialog" aria-label="Close" type="button" data-view-component="true" class="close-button Overlay-closeButton"><svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-x">
    <path d="M3.72 3.72a.75.75 0 0 1 1.06 0L8 6.94l3.22-3.22a.749.749 0 0 1 1.275.326.749.749 0 0 1-.215.734L9.06 8l3.22 3.22a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L8 9.06l-3.22 3.22a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042L6.94 8 3.72 4.78a.75.75 0 0 1 0-1.06Z"></path>
</svg></button>
    </div>
  </div>
  
</div>
      <scrollable-region data-labelled-by="feedback-dialog-title" data-catalyst="" style="overflow: auto;">
        <div data-view-component="true" class="Overlay-body">        <!-- '"` --><!-- </textarea></xmp> --><form id="code-search-feedback-form" data-turbo="false" action="https://github.com/search/feedback" accept-charset="UTF-8" method="post"><input type="hidden" name="authenticity_token" value="4cUD8uvqk56uvjk2Hgp3uolAiWfs9Gwg1zYlvhZx_4lsHMwH23cw5gVWlsJYh7lw0Bvd7IctrdPquyP56QC6bw">
          <p>We read every piece of feedback, and take your input very seriously.</p>
          <textarea name="feedback" class="form-control width-full mb-2" style="height: 120px" id="feedback"></textarea>
          <input name="include_email" id="include_email" aria-label="Include my email address so I can be contacted" class="form-control mr-2" type="checkbox">
          <label for="include_email" style="font-weight: normal">Include my email address so I can be contacted</label>
</form></div>
      </scrollable-region>
      <div data-view-component="true" class="Overlay-footer Overlay-footer--alignEnd">          <button data-close-dialog-id="feedback-dialog" type="button" data-view-component="true" class="btn">    Cancel
</button>
          <button form="code-search-feedback-form" data-action="click:qbsearch-input#submitFeedback" type="submit" data-view-component="true" class="btn-primary btn">    Submit feedback
</button>
</div>
</dialog></dialog-helper>

    <custom-scopes data-target="qbsearch-input.customScopesManager" data-catalyst="">
    
<dialog-helper>
  <dialog data-target="custom-scopes.customScopesModalDialog" data-action="close:qbsearch-input#handleDialogClose cancel:qbsearch-input#handleDialogClose" id="custom-scopes-dialog" aria-modal="true" aria-labelledby="custom-scopes-dialog-title" aria-describedby="custom-scopes-dialog-description" data-view-component="true" class="Overlay Overlay-whenNarrow Overlay--size-medium Overlay--motion-scaleFade Overlay--disableScroll">
    <div data-view-component="true" class="Overlay-header Overlay-header--divided">
  <div class="Overlay-headerContentWrap">
    <div class="Overlay-titleWrap">
      <h1 class="Overlay-title " id="custom-scopes-dialog-title">
        Saved searches
      </h1>
        <h2 id="custom-scopes-dialog-description" class="Overlay-description">Use saved searches to filter your results more quickly</h2>
    </div>
    <div class="Overlay-actionWrap">
      <button data-close-dialog-id="custom-scopes-dialog" aria-label="Close" type="button" data-view-component="true" class="close-button Overlay-closeButton"><svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-x">
    <path d="M3.72 3.72a.75.75 0 0 1 1.06 0L8 6.94l3.22-3.22a.749.749 0 0 1 1.275.326.749.749 0 0 1-.215.734L9.06 8l3.22 3.22a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L8 9.06l-3.22 3.22a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042L6.94 8 3.72 4.78a.75.75 0 0 1 0-1.06Z"></path>
</svg></button>
    </div>
  </div>
  
</div>
      <scrollable-region data-labelled-by="custom-scopes-dialog-title" data-catalyst="" style="overflow: auto;">
        <div data-view-component="true" class="Overlay-body">        <div data-target="custom-scopes.customScopesModalDialogFlash"></div>

        <div hidden="" class="create-custom-scope-form" data-target="custom-scopes.createCustomScopeForm">
        <!-- '"` --><!-- </textarea></xmp> --><form id="custom-scopes-dialog-form" data-turbo="false" action="https://github.com/search/custom_scopes" accept-charset="UTF-8" method="post"><input type="hidden" name="authenticity_token" value="AzrTIBnbMGvX3OOqt7KjZ1mhUaeWb05Wz258Cup4Jj1gfGT7536kLC8CLQ4Pr83XmVGADswMDG4CZ1zAval6lQ">
          <div data-target="custom-scopes.customScopesModalDialogFlash"></div>

          <input type="hidden" id="custom_scope_id" name="custom_scope_id" data-target="custom-scopes.customScopesIdField">

          <div class="form-group">
            <label for="custom_scope_name">Name</label>
            <auto-check src="/search/custom_scopes/check_name" required="">
              <input type="text" name="custom_scope_name" id="custom_scope_name" data-target="custom-scopes.customScopesNameField" class="form-control" autocomplete="off" placeholder="github-ruby" required="" maxlength="50" spellcheck="false">
              <input type="hidden" value="omn2NSzkq6XmXuBRmzKbgx1qlZPSEkARWK-TJ1YnIyTfxUwAZSKL-rfnWqDKUUjpDenC3VXHZogbmI1_IbeJjQ" data-csrf="true">
            </auto-check>
          </div>

          <div class="form-group">
            <label for="custom_scope_query">Query</label>
            <input type="text" name="custom_scope_query" id="custom_scope_query" data-target="custom-scopes.customScopesQueryField" class="form-control" autocomplete="off" placeholder="(repo:mona/a OR repo:mona/b) AND lang:python" required="" maxlength="500">
          </div>

          <p class="text-small color-fg-muted">
            To see all available qualifiers, see our <a class="Link--inTextBlock" href="https://docs.github.com/search-github/github-code-search/understanding-github-code-search-syntax">documentation</a>.
          </p>
</form>        </div>

        <div data-target="custom-scopes.manageCustomScopesForm">
          <div data-target="custom-scopes.list"></div>
        </div>

</div>
      </scrollable-region>
      <div data-view-component="true" class="Overlay-footer Overlay-footer--alignEnd Overlay-footer--divided">          <button data-action="click:custom-scopes#customScopesCancel" type="button" data-view-component="true" class="btn">    Cancel
</button>
          <button form="custom-scopes-dialog-form" data-action="click:custom-scopes#customScopesSubmit" data-target="custom-scopes.customScopesSubmitButton" type="submit" data-view-component="true" class="btn-primary btn">    Create saved search
</button>
</div>
</dialog></dialog-helper>
    </custom-scopes>
  </div>
</qbsearch-input>    <input type="hidden" value="seN6BKXPT5gBcRvW1cEtDTYLZPgbjP_npJsQGXJryKoWTeCXedTGFq_f_1novhctwXJ3DGzvEBBZNt58yNMO2Q" data-csrf="true" class="js-data-jump-to-suggestions-path-csrf">

          </div>

        

        <div class="AppHeader-actions position-relative">
             <react-partial-anchor data-catalyst="">
      <button id="global-create-menu-anchor" aria-label="Create something new" data-target="react-partial-anchor.anchor" type="button" data-view-component="true" class="AppHeader-button global-create-button Button--secondary Button--medium Button width-auto color-fg-muted" aria-describedby="tooltip-f213bd56-15e8-434b-8f91-5035a4e8526c" aria-expanded="false" aria-haspopup="true">  <span class="Button-content">
      <span class="Button-visual Button-leadingVisual">
        <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
      </span>
    <span class="Button-label"><svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-triangle-down">
    <path d="m4.427 7.427 3.396 3.396a.25.25 0 0 0 .354 0l3.396-3.396A.25.25 0 0 0 11.396 7H4.604a.25.25 0 0 0-.177.427Z"></path>
</svg></span>
  </span>
</button><tool-tip id="tooltip-f213bd56-15e8-434b-8f91-5035a4e8526c" for="global-create-menu-anchor" popover="manual" data-direction="s" data-type="description" data-view-component="true" class="sr-only position-absolute" role="tooltip"><template shadowrootmode="open"><style>
      :host {
        --tooltip-top: var(--tool-tip-position-top, 0);
        --tooltip-left: var(--tool-tip-position-left, 0);
        padding: var(--overlay-paddingBlock-condensed) var(--overlay-padding-condensed) !important;
        font: var(--text-body-shorthand-small);
        color: var(--tooltip-fgColor, var(--fgColor-onEmphasis)) !important;
        text-align: center;
        text-decoration: none;
        text-shadow: none;
        text-transform: none;
        letter-spacing: normal;
        word-wrap: break-word;
        white-space: pre;
        background: var(--tooltip-bgColor, var(--bgColor-emphasis)) !important;
        border-radius: var(--borderRadius-medium);
        border: 0 !important;
        opacity: 0;
        max-width: var(--overlay-width-small);
        word-wrap: break-word;
        white-space: normal;
        width: max-content !important;
        inset: var(--tooltip-top) auto auto var(--tooltip-left) !important;
        overflow: visible !important;
        text-wrap: balance;
      }

      :host(:is(.tooltip-n, .tooltip-nw, .tooltip-ne)) {
        --tooltip-top: calc(var(--tool-tip-position-top, 0) - var(--overlay-offset, 0.25rem));
        --tooltip-left: var(--tool-tip-position-left);
      }

      :host(:is(.tooltip-s, .tooltip-sw, .tooltip-se)) {
        --tooltip-top: calc(var(--tool-tip-position-top, 0) + var(--overlay-offset, 0.25rem));
        --tooltip-left: var(--tool-tip-position-left);
      }

      :host(.tooltip-w) {
        --tooltip-top: var(--tool-tip-position-top);
        --tooltip-left: calc(var(--tool-tip-position-left, 0) - var(--overlay-offset, 0.25rem));
      }

      :host(.tooltip-e) {
        --tooltip-top: var(--tool-tip-position-top);
        --tooltip-left: calc(var(--tool-tip-position-left, 0) + var(--overlay-offset, 0.25rem));
      }

      :host:after{
        position: absolute;
        display: block;
        right: 0;
        left: 0;
        height: var(--overlay-offset, 0.25rem);
        content: "";
      }

      :host(.tooltip-s):after,
      :host(.tooltip-se):after,
      :host(.tooltip-sw):after {
        bottom: 100%
      }

      :host(.tooltip-n):after,
      :host(.tooltip-ne):after,
      :host(.tooltip-nw):after {
        top: 100%;
      }

      @keyframes tooltip-appear {
        from {
          opacity: 0;
        }
        to {
          opacity: 1;
        }
      }

      :host(:popover-open),
      :host(:popover-open):before {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      :host(.\:popover-open) {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      @media (forced-colors: active) {
        :host {
          outline: solid 1px transparent;
        }

        :host:before {
          display: none;
        }
      }
    </style><slot></slot></template>Create new...</tool-tip>

      
    
        <script crossorigin="anonymous" defer="defer" type="application/javascript" src="./app_files/ui_packages_promise-with-resolvers-polyfill_promise-with-resolvers-polyfill_ts-ui_packages_re-8d43b0-1d71e4cf38e3.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./app_files/global-create-menu-e66a8207c01b.js.download"></script>
<link crossorigin="anonymous" media="all" rel="stylesheet" href="./app_files/primer-react.9fa170e9435ed4b922b9.module.css">

<react-partial partial-name="global-create-menu" data-ssr="false" data-attempted-ssr="false" data-catalyst="" class="loaded">
  
  <script type="application/json" data-target="react-partial.embeddedData">{"props":{"createRepo":true,"importRepo":true,"codespaces":true,"gist":true,"createOrg":true,"createProject":false,"createProjectUrl":"/Malaika-Mustafa?tab=projects","createLegacyProject":false,"createIssue":false,"org":null,"owner":"SumaikaImran","repo":"AI_LABS"}}</script>
  <div data-target="react-partial.reactRoot"><script type="application/json" id="__PRIMER_DATA_:r14:__">{"resolvedServerColorMode":"day"}</script></div>
</react-partial>

      </react-partial-anchor>


          <a href="https://github.com/issues" data-analytics-event="{&quot;category&quot;:&quot;Global navigation&quot;,&quot;action&quot;:&quot;ISSUES_HEADER&quot;,&quot;label&quot;:null}" id="icon-button-20e456ee-1633-4cdf-a305-78f7bfaacf83" aria-labelledby="tooltip-66f15e4b-39c3-4ebf-9eb0-7f2f492c19f2" data-view-component="true" class="Button Button--iconOnly Button--secondary Button--medium AppHeader-button color-fg-muted">  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-issue-opened Button-visual">
    <path d="M8 9.5a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Z"></path><path d="M8 0a8 8 0 1 1 0 16A8 8 0 0 1 8 0ZM1.5 8a6.5 6.5 0 1 0 13 0 6.5 6.5 0 0 0-13 0Z"></path>
</svg>
</a><tool-tip id="tooltip-66f15e4b-39c3-4ebf-9eb0-7f2f492c19f2" for="icon-button-20e456ee-1633-4cdf-a305-78f7bfaacf83" popover="manual" data-direction="s" data-type="label" data-view-component="true" class="sr-only position-absolute" aria-hidden="true" role="tooltip"><template shadowrootmode="open"><style>
      :host {
        --tooltip-top: var(--tool-tip-position-top, 0);
        --tooltip-left: var(--tool-tip-position-left, 0);
        padding: var(--overlay-paddingBlock-condensed) var(--overlay-padding-condensed) !important;
        font: var(--text-body-shorthand-small);
        color: var(--tooltip-fgColor, var(--fgColor-onEmphasis)) !important;
        text-align: center;
        text-decoration: none;
        text-shadow: none;
        text-transform: none;
        letter-spacing: normal;
        word-wrap: break-word;
        white-space: pre;
        background: var(--tooltip-bgColor, var(--bgColor-emphasis)) !important;
        border-radius: var(--borderRadius-medium);
        border: 0 !important;
        opacity: 0;
        max-width: var(--overlay-width-small);
        word-wrap: break-word;
        white-space: normal;
        width: max-content !important;
        inset: var(--tooltip-top) auto auto var(--tooltip-left) !important;
        overflow: visible !important;
        text-wrap: balance;
      }

      :host(:is(.tooltip-n, .tooltip-nw, .tooltip-ne)) {
        --tooltip-top: calc(var(--tool-tip-position-top, 0) - var(--overlay-offset, 0.25rem));
        --tooltip-left: var(--tool-tip-position-left);
      }

      :host(:is(.tooltip-s, .tooltip-sw, .tooltip-se)) {
        --tooltip-top: calc(var(--tool-tip-position-top, 0) + var(--overlay-offset, 0.25rem));
        --tooltip-left: var(--tool-tip-position-left);
      }

      :host(.tooltip-w) {
        --tooltip-top: var(--tool-tip-position-top);
        --tooltip-left: calc(var(--tool-tip-position-left, 0) - var(--overlay-offset, 0.25rem));
      }

      :host(.tooltip-e) {
        --tooltip-top: var(--tool-tip-position-top);
        --tooltip-left: calc(var(--tool-tip-position-left, 0) + var(--overlay-offset, 0.25rem));
      }

      :host:after{
        position: absolute;
        display: block;
        right: 0;
        left: 0;
        height: var(--overlay-offset, 0.25rem);
        content: "";
      }

      :host(.tooltip-s):after,
      :host(.tooltip-se):after,
      :host(.tooltip-sw):after {
        bottom: 100%
      }

      :host(.tooltip-n):after,
      :host(.tooltip-ne):after,
      :host(.tooltip-nw):after {
        top: 100%;
      }

      @keyframes tooltip-appear {
        from {
          opacity: 0;
        }
        to {
          opacity: 1;
        }
      }

      :host(:popover-open),
      :host(:popover-open):before {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      :host(.\:popover-open) {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      @media (forced-colors: active) {
        :host {
          outline: solid 1px transparent;
        }

        :host:before {
          display: none;
        }
      }
    </style><slot></slot></template>Issues</tool-tip>

          <a href="https://github.com/pulls" data-analytics-event="{&quot;category&quot;:&quot;Global navigation&quot;,&quot;action&quot;:&quot;PULL_REQUESTS_HEADER&quot;,&quot;label&quot;:null}" id="icon-button-76071d14-be56-4557-afde-670abe445a99" aria-labelledby="tooltip-1823039c-88cd-49c4-ad35-8d2c6e98de14" data-view-component="true" class="Button Button--iconOnly Button--secondary Button--medium AppHeader-button color-fg-muted">  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-git-pull-request Button-visual">
    <path d="M1.5 3.25a2.25 2.25 0 1 1 3 2.122v5.256a2.251 2.251 0 1 1-1.5 0V5.372A2.25 2.25 0 0 1 1.5 3.25Zm5.677-.177L9.573.677A.25.25 0 0 1 10 .854V2.5h1A2.5 2.5 0 0 1 13.5 5v5.628a2.251 2.251 0 1 1-1.5 0V5a1 1 0 0 0-1-1h-1v1.646a.25.25 0 0 1-.427.177L7.177 3.427a.25.25 0 0 1 0-.354ZM3.75 2.5a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5Zm0 9.5a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5Zm8.25.75a.75.75 0 1 0 1.5 0 .75.75 0 0 0-1.5 0Z"></path>
</svg>
</a><tool-tip id="tooltip-1823039c-88cd-49c4-ad35-8d2c6e98de14" for="icon-button-76071d14-be56-4557-afde-670abe445a99" popover="manual" data-direction="s" data-type="label" data-view-component="true" class="sr-only position-absolute" aria-hidden="true" role="tooltip"><template shadowrootmode="open"><style>
      :host {
        --tooltip-top: var(--tool-tip-position-top, 0);
        --tooltip-left: var(--tool-tip-position-left, 0);
        padding: var(--overlay-paddingBlock-condensed) var(--overlay-padding-condensed) !important;
        font: var(--text-body-shorthand-small);
        color: var(--tooltip-fgColor, var(--fgColor-onEmphasis)) !important;
        text-align: center;
        text-decoration: none;
        text-shadow: none;
        text-transform: none;
        letter-spacing: normal;
        word-wrap: break-word;
        white-space: pre;
        background: var(--tooltip-bgColor, var(--bgColor-emphasis)) !important;
        border-radius: var(--borderRadius-medium);
        border: 0 !important;
        opacity: 0;
        max-width: var(--overlay-width-small);
        word-wrap: break-word;
        white-space: normal;
        width: max-content !important;
        inset: var(--tooltip-top) auto auto var(--tooltip-left) !important;
        overflow: visible !important;
        text-wrap: balance;
      }

      :host(:is(.tooltip-n, .tooltip-nw, .tooltip-ne)) {
        --tooltip-top: calc(var(--tool-tip-position-top, 0) - var(--overlay-offset, 0.25rem));
        --tooltip-left: var(--tool-tip-position-left);
      }

      :host(:is(.tooltip-s, .tooltip-sw, .tooltip-se)) {
        --tooltip-top: calc(var(--tool-tip-position-top, 0) + var(--overlay-offset, 0.25rem));
        --tooltip-left: var(--tool-tip-position-left);
      }

      :host(.tooltip-w) {
        --tooltip-top: var(--tool-tip-position-top);
        --tooltip-left: calc(var(--tool-tip-position-left, 0) - var(--overlay-offset, 0.25rem));
      }

      :host(.tooltip-e) {
        --tooltip-top: var(--tool-tip-position-top);
        --tooltip-left: calc(var(--tool-tip-position-left, 0) + var(--overlay-offset, 0.25rem));
      }

      :host:after{
        position: absolute;
        display: block;
        right: 0;
        left: 0;
        height: var(--overlay-offset, 0.25rem);
        content: "";
      }

      :host(.tooltip-s):after,
      :host(.tooltip-se):after,
      :host(.tooltip-sw):after {
        bottom: 100%
      }

      :host(.tooltip-n):after,
      :host(.tooltip-ne):after,
      :host(.tooltip-nw):after {
        top: 100%;
      }

      @keyframes tooltip-appear {
        from {
          opacity: 0;
        }
        to {
          opacity: 1;
        }
      }

      :host(:popover-open),
      :host(:popover-open):before {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      :host(.\:popover-open) {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      @media (forced-colors: active) {
        :host {
          outline: solid 1px transparent;
        }

        :host:before {
          display: none;
        }
      }
    </style><slot></slot></template>Pull requests</tool-tip>

        </div>

        <notification-indicator data-channel="eyJjIjoibm90aWZpY2F0aW9uLWNoYW5nZWQ6MTQ2MDYzODE0IiwidCI6MTczMjg1MjM2Nn0=--0c140f91799b8d1f7240cfdbf4c7318c480adc1d33f3bb8aca8388b183389a06" data-indicator-mode="none" data-tooltip-global="You have unread notifications" data-tooltip-unavailable="Notifications are unavailable at the moment." data-tooltip-none="You have no unread notifications" data-header-redesign-enabled="true" data-fetch-indicator-src="/notifications/indicator" data-fetch-indicator-enabled="true" data-view-component="true" class="js-socket-channel" data-fetch-retry-delay-time="500" data-catalyst="">
    <a id="AppHeader-notifications-button" href="https://github.com/notifications" aria-labelledby="notification-indicator-tooltip" data-hotkey="g n" data-target="notification-indicator.link" data-analytics-event="{&quot;category&quot;:&quot;Global navigation&quot;,&quot;action&quot;:&quot;NOTIFICATIONS_HEADER&quot;,&quot;label&quot;:&quot;icon:read&quot;}" data-view-component="true" class="Button Button--iconOnly Button--secondary Button--medium AppHeader-button color-fg-muted">  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-inbox Button-visual">
    <path d="M2.8 2.06A1.75 1.75 0 0 1 4.41 1h7.18c.7 0 1.333.417 1.61 1.06l2.74 6.395c.04.093.06.194.06.295v4.5A1.75 1.75 0 0 1 14.25 15H1.75A1.75 1.75 0 0 1 0 13.25v-4.5c0-.101.02-.202.06-.295Zm1.61.44a.25.25 0 0 0-.23.152L1.887 8H4.75a.75.75 0 0 1 .6.3L6.625 10h2.75l1.275-1.7a.75.75 0 0 1 .6-.3h2.863L11.82 2.652a.25.25 0 0 0-.23-.152Zm10.09 7h-2.875l-1.275 1.7a.75.75 0 0 1-.6.3h-3.5a.75.75 0 0 1-.6-.3L4.375 9.5H1.5v3.75c0 .138.112.25.25.25h12.5a.25.25 0 0 0 .25-.25Z"></path>
</svg>
</a>

    <tool-tip id="notification-indicator-tooltip" data-target="notification-indicator.tooltip" for="AppHeader-notifications-button" popover="manual" data-direction="s" data-type="label" data-view-component="true" class="sr-only position-absolute" aria-hidden="true" role="tooltip"><template shadowrootmode="open"><style>
      :host {
        --tooltip-top: var(--tool-tip-position-top, 0);
        --tooltip-left: var(--tool-tip-position-left, 0);
        padding: var(--overlay-paddingBlock-condensed) var(--overlay-padding-condensed) !important;
        font: var(--text-body-shorthand-small);
        color: var(--tooltip-fgColor, var(--fgColor-onEmphasis)) !important;
        text-align: center;
        text-decoration: none;
        text-shadow: none;
        text-transform: none;
        letter-spacing: normal;
        word-wrap: break-word;
        white-space: pre;
        background: var(--tooltip-bgColor, var(--bgColor-emphasis)) !important;
        border-radius: var(--borderRadius-medium);
        border: 0 !important;
        opacity: 0;
        max-width: var(--overlay-width-small);
        word-wrap: break-word;
        white-space: normal;
        width: max-content !important;
        inset: var(--tooltip-top) auto auto var(--tooltip-left) !important;
        overflow: visible !important;
        text-wrap: balance;
      }

      :host(:is(.tooltip-n, .tooltip-nw, .tooltip-ne)) {
        --tooltip-top: calc(var(--tool-tip-position-top, 0) - var(--overlay-offset, 0.25rem));
        --tooltip-left: var(--tool-tip-position-left);
      }

      :host(:is(.tooltip-s, .tooltip-sw, .tooltip-se)) {
        --tooltip-top: calc(var(--tool-tip-position-top, 0) + var(--overlay-offset, 0.25rem));
        --tooltip-left: var(--tool-tip-position-left);
      }

      :host(.tooltip-w) {
        --tooltip-top: var(--tool-tip-position-top);
        --tooltip-left: calc(var(--tool-tip-position-left, 0) - var(--overlay-offset, 0.25rem));
      }

      :host(.tooltip-e) {
        --tooltip-top: var(--tool-tip-position-top);
        --tooltip-left: calc(var(--tool-tip-position-left, 0) + var(--overlay-offset, 0.25rem));
      }

      :host:after{
        position: absolute;
        display: block;
        right: 0;
        left: 0;
        height: var(--overlay-offset, 0.25rem);
        content: "";
      }

      :host(.tooltip-s):after,
      :host(.tooltip-se):after,
      :host(.tooltip-sw):after {
        bottom: 100%
      }

      :host(.tooltip-n):after,
      :host(.tooltip-ne):after,
      :host(.tooltip-nw):after {
        top: 100%;
      }

      @keyframes tooltip-appear {
        from {
          opacity: 0;
        }
        to {
          opacity: 1;
        }
      }

      :host(:popover-open),
      :host(:popover-open):before {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      :host(.\:popover-open) {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      @media (forced-colors: active) {
        :host {
          outline: solid 1px transparent;
        }

        :host:before {
          display: none;
        }
      }
    </style><slot></slot></template>You have no unread notifications</tool-tip>
</notification-indicator>

        <div class="AppHeader-user">
          <deferred-side-panel data-url="/_side-panels/user?repository_id=871997669" data-catalyst="">
  <include-fragment data-target="deferred-side-panel.fragment"><template shadowrootmode="open"><style>:host {display: block;}</style><slot></slot></template>
    <react-partial-anchor data-catalyst="">
  <button data-target="react-partial-anchor.anchor" data-login="Malaika-Mustafa" aria-label="Open user navigation menu" type="button" data-view-component="true" class="Button--invisible Button--medium Button Button--invisible-noVisuals color-bg-transparent p-0" aria-expanded="false" aria-haspopup="true">  <span class="Button-content">
    <span class="Button-label"><img src="./app_files/146063814" alt="" size="32" height="32" width="32" data-view-component="true" class="avatar circle"></span>
  </span>
</button>
  

    <script crossorigin="anonymous" defer="defer" type="application/javascript" src="./app_files/global-user-nav-drawer-ff0112d1e697.js.download"></script>
<link crossorigin="anonymous" media="all" rel="stylesheet" href="./app_files/primer-react.9fa170e9435ed4b922b9.module.css">
<link crossorigin="anonymous" media="all" rel="stylesheet" href="./app_files/global-user-nav-drawer.830d6c10c9fea7fc134e.module.css">

<react-partial partial-name="global-user-nav-drawer" data-ssr="false" data-attempted-ssr="false" data-catalyst="" class="loaded">
  
  <script type="application/json" data-target="react-partial.embeddedData">{"props":{"owner":{"login":"Malaika-Mustafa","name":null,"avatarUrl":"https://avatars.githubusercontent.com/u/146063814?v=4"},"drawerId":"global-user-nav-drawer","lazyLoadItemDataFetchUrl":"/_side-panels/user.json","canAddAccount":true,"addAccountPath":"/login?add_account=1\u0026return_to=https%3A%2F%2Fgithub.com%2FSumaikaImran%2FAI_LABS%2Fblob%2Fmain%2Fapp.py","switchAccountPath":"/switch_account","loginAccountPath":"/login?add_account=1","projectsPath":"/Malaika-Mustafa?tab=projects","gistsUrl":"https://gist.github.com/mine","docsUrl":"https://docs.github.com","yourEnterpriseUrl":null,"enterpriseSettingsUrl":null,"supportUrl":"https://support.github.com","showAccountSwitcher":true,"showCopilot":true,"showEnterprises":true,"showEnterprise":false,"showGists":true,"showOrganizations":true,"showSponsors":true,"showUpgrade":true,"showFeaturesPreviews":true,"showEnterpriseSettings":false,"createMenuProps":{"createRepo":true,"importRepo":true,"codespaces":true,"gist":true,"createOrg":true,"createProject":false,"createProjectUrl":"/Malaika-Mustafa?tab=projects","createLegacyProject":false,"createIssue":false,"org":null,"owner":"SumaikaImran","repo":"AI_LABS"}}}</script>
  <div data-target="react-partial.reactRoot"><script type="application/json" id="__PRIMER_DATA_:r17:__">{"resolvedServerColorMode":"day"}</script></div>
</react-partial>

  </react-partial-anchor>

  </include-fragment>
</deferred-side-panel>
        </div>

        <div class="position-absolute mt-2">
            
<site-header-logged-in-user-menu data-catalyst="">

</site-header-logged-in-user-menu>

        </div>
      </div>
    </div>


      <div class="AppHeader-localBar">
        <nav data-pjax="#js-repo-pjax-container" aria-label="Repository" data-view-component="true" class="js-repo-nav js-sidenav-container-pjax js-responsive-underlinenav overflow-hidden UnderlineNav">

  <ul data-view-component="true" class="UnderlineNav-body list-style-none">
      <li data-view-component="true" class="d-inline-flex">
  <a id="code-tab" href="https://github.com/SumaikaImran/AI_LABS" data-tab-item="i0code-tab" data-selected-links="repo_source repo_downloads repo_commits repo_releases repo_tags repo_branches repo_packages repo_deployments repo_attestations /SumaikaImran/AI_LABS" data-pjax="#repo-content-pjax-container" data-turbo-frame="repo-content-turbo-frame" data-hotkey="g c" data-analytics-event="{&quot;category&quot;:&quot;Underline navbar&quot;,&quot;action&quot;:&quot;Click tab&quot;,&quot;label&quot;:&quot;Code&quot;,&quot;target&quot;:&quot;UNDERLINE_NAV.TAB&quot;}" data-view-component="true" class="UnderlineNav-item no-wrap js-responsive-underlinenav-item js-selected-navigation-item selected" aria-current="page">
    
              <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-code UnderlineNav-octicon d-none d-sm-inline">
    <path d="m11.28 3.22 4.25 4.25a.75.75 0 0 1 0 1.06l-4.25 4.25a.749.749 0 0 1-1.275-.326.749.749 0 0 1 .215-.734L13.94 8l-3.72-3.72a.749.749 0 0 1 .326-1.275.749.749 0 0 1 .734.215Zm-6.56 0a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042L2.06 8l3.72 3.72a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L.47 8.53a.75.75 0 0 1 0-1.06Z"></path>
</svg>
        <span data-content="Code">Code</span>
          <span id="code-repo-tab-count" data-pjax-replace="" data-turbo-replace="" title="Not available" data-view-component="true" class="Counter"></span>


    
</a></li>
      <li data-view-component="true" class="d-inline-flex">
  <a id="issues-tab" href="https://github.com/SumaikaImran/AI_LABS/issues" data-tab-item="i1issues-tab" data-selected-links="repo_issues repo_labels repo_milestones /SumaikaImran/AI_LABS/issues" data-pjax="#repo-content-pjax-container" data-turbo-frame="repo-content-turbo-frame" data-hotkey="g i" data-analytics-event="{&quot;category&quot;:&quot;Underline navbar&quot;,&quot;action&quot;:&quot;Click tab&quot;,&quot;label&quot;:&quot;Issues&quot;,&quot;target&quot;:&quot;UNDERLINE_NAV.TAB&quot;}" data-view-component="true" class="UnderlineNav-item no-wrap js-responsive-underlinenav-item js-selected-navigation-item">
    
              <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-issue-opened UnderlineNav-octicon d-none d-sm-inline">
    <path d="M8 9.5a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Z"></path><path d="M8 0a8 8 0 1 1 0 16A8 8 0 0 1 8 0ZM1.5 8a6.5 6.5 0 1 0 13 0 6.5 6.5 0 0 0-13 0Z"></path>
</svg>
        <span data-content="Issues">Issues</span>
          <span id="issues-repo-tab-count" data-pjax-replace="" data-turbo-replace="" title="0" hidden="hidden" data-view-component="true" class="Counter">0</span>


    
</a></li>
      <li data-view-component="true" class="d-inline-flex">
  <a id="pull-requests-tab" href="https://github.com/SumaikaImran/AI_LABS/pulls" data-tab-item="i2pull-requests-tab" data-selected-links="repo_pulls checks /SumaikaImran/AI_LABS/pulls" data-pjax="#repo-content-pjax-container" data-turbo-frame="repo-content-turbo-frame" data-hotkey="g p" data-analytics-event="{&quot;category&quot;:&quot;Underline navbar&quot;,&quot;action&quot;:&quot;Click tab&quot;,&quot;label&quot;:&quot;Pull requests&quot;,&quot;target&quot;:&quot;UNDERLINE_NAV.TAB&quot;}" data-view-component="true" class="UnderlineNav-item no-wrap js-responsive-underlinenav-item js-selected-navigation-item">
    
              <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-git-pull-request UnderlineNav-octicon d-none d-sm-inline">
    <path d="M1.5 3.25a2.25 2.25 0 1 1 3 2.122v5.256a2.251 2.251 0 1 1-1.5 0V5.372A2.25 2.25 0 0 1 1.5 3.25Zm5.677-.177L9.573.677A.25.25 0 0 1 10 .854V2.5h1A2.5 2.5 0 0 1 13.5 5v5.628a2.251 2.251 0 1 1-1.5 0V5a1 1 0 0 0-1-1h-1v1.646a.25.25 0 0 1-.427.177L7.177 3.427a.25.25 0 0 1 0-.354ZM3.75 2.5a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5Zm0 9.5a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5Zm8.25.75a.75.75 0 1 0 1.5 0 .75.75 0 0 0-1.5 0Z"></path>
</svg>
        <span data-content="Pull requests">Pull requests</span>
          <span id="pull-requests-repo-tab-count" data-pjax-replace="" data-turbo-replace="" title="0" hidden="hidden" data-view-component="true" class="Counter">0</span>


    
</a></li>
      <li data-view-component="true" class="d-inline-flex">
  <a id="actions-tab" href="https://github.com/SumaikaImran/AI_LABS/actions" data-tab-item="i3actions-tab" data-selected-links="repo_actions /SumaikaImran/AI_LABS/actions" data-pjax="#repo-content-pjax-container" data-turbo-frame="repo-content-turbo-frame" data-hotkey="g a" data-analytics-event="{&quot;category&quot;:&quot;Underline navbar&quot;,&quot;action&quot;:&quot;Click tab&quot;,&quot;label&quot;:&quot;Actions&quot;,&quot;target&quot;:&quot;UNDERLINE_NAV.TAB&quot;}" data-view-component="true" class="UnderlineNav-item no-wrap js-responsive-underlinenav-item js-selected-navigation-item">
    
              <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-play UnderlineNav-octicon d-none d-sm-inline">
    <path d="M8 0a8 8 0 1 1 0 16A8 8 0 0 1 8 0ZM1.5 8a6.5 6.5 0 1 0 13 0 6.5 6.5 0 0 0-13 0Zm4.879-2.773 4.264 2.559a.25.25 0 0 1 0 .428l-4.264 2.559A.25.25 0 0 1 6 10.559V5.442a.25.25 0 0 1 .379-.215Z"></path>
</svg>
        <span data-content="Actions">Actions</span>
          <span id="actions-repo-tab-count" data-pjax-replace="" data-turbo-replace="" title="Not available" data-view-component="true" class="Counter"></span>


    
</a></li>
      <li data-view-component="true" class="d-inline-flex">
  <a id="projects-tab" href="https://github.com/SumaikaImran/AI_LABS/projects" data-tab-item="i4projects-tab" data-selected-links="repo_projects new_repo_project repo_project /SumaikaImran/AI_LABS/projects" data-pjax="#repo-content-pjax-container" data-turbo-frame="repo-content-turbo-frame" data-hotkey="g b" data-analytics-event="{&quot;category&quot;:&quot;Underline navbar&quot;,&quot;action&quot;:&quot;Click tab&quot;,&quot;label&quot;:&quot;Projects&quot;,&quot;target&quot;:&quot;UNDERLINE_NAV.TAB&quot;}" data-view-component="true" class="UnderlineNav-item no-wrap js-responsive-underlinenav-item js-selected-navigation-item">
    
              <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-table UnderlineNav-octicon d-none d-sm-inline">
    <path d="M0 1.75C0 .784.784 0 1.75 0h12.5C15.216 0 16 .784 16 1.75v12.5A1.75 1.75 0 0 1 14.25 16H1.75A1.75 1.75 0 0 1 0 14.25ZM6.5 6.5v8h7.75a.25.25 0 0 0 .25-.25V6.5Zm8-1.5V1.75a.25.25 0 0 0-.25-.25H6.5V5Zm-13 1.5v7.75c0 .138.112.25.25.25H5v-8ZM5 5V1.5H1.75a.25.25 0 0 0-.25.25V5Z"></path>
</svg>
        <span data-content="Projects">Projects</span>
          <span id="projects-repo-tab-count" data-pjax-replace="" data-turbo-replace="" title="0" hidden="hidden" data-view-component="true" class="Counter">0</span>


    
</a></li>
      <li data-view-component="true" class="d-inline-flex">
  <a id="security-tab" href="https://github.com/SumaikaImran/AI_LABS/security" data-tab-item="i5security-tab" data-selected-links="security overview alerts policy token_scanning code_scanning /SumaikaImran/AI_LABS/security" data-pjax="#repo-content-pjax-container" data-turbo-frame="repo-content-turbo-frame" data-hotkey="g s" data-analytics-event="{&quot;category&quot;:&quot;Underline navbar&quot;,&quot;action&quot;:&quot;Click tab&quot;,&quot;label&quot;:&quot;Security&quot;,&quot;target&quot;:&quot;UNDERLINE_NAV.TAB&quot;}" data-view-component="true" class="UnderlineNav-item no-wrap js-responsive-underlinenav-item js-selected-navigation-item">
    
              <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-shield UnderlineNav-octicon d-none d-sm-inline">
    <path d="M7.467.133a1.748 1.748 0 0 1 1.066 0l5.25 1.68A1.75 1.75 0 0 1 15 3.48V7c0 1.566-.32 3.182-1.303 4.682-.983 1.498-2.585 2.813-5.032 3.855a1.697 1.697 0 0 1-1.33 0c-2.447-1.042-4.049-2.357-5.032-3.855C1.32 10.182 1 8.566 1 7V3.48a1.75 1.75 0 0 1 1.217-1.667Zm.61 1.429a.25.25 0 0 0-.153 0l-5.25 1.68a.25.25 0 0 0-.174.238V7c0 1.358.275 2.666 1.057 3.86.784 1.194 2.121 2.34 4.366 3.297a.196.196 0 0 0 .154 0c2.245-.956 3.582-2.104 4.366-3.298C13.225 9.666 13.5 8.36 13.5 7V3.48a.251.251 0 0 0-.174-.237l-5.25-1.68ZM8.75 4.75v3a.75.75 0 0 1-1.5 0v-3a.75.75 0 0 1 1.5 0ZM9 10.5a1 1 0 1 1-2 0 1 1 0 0 1 2 0Z"></path>
</svg>
        <span data-content="Security">Security</span>
          

    
</a></li>
      <li data-view-component="true" class="d-inline-flex">
  <a id="insights-tab" href="https://github.com/SumaikaImran/AI_LABS/pulse" data-tab-item="i6insights-tab" data-selected-links="repo_graphs repo_contributors dependency_graph dependabot_updates pulse people community /SumaikaImran/AI_LABS/pulse" data-pjax="#repo-content-pjax-container" data-turbo-frame="repo-content-turbo-frame" data-analytics-event="{&quot;category&quot;:&quot;Underline navbar&quot;,&quot;action&quot;:&quot;Click tab&quot;,&quot;label&quot;:&quot;Insights&quot;,&quot;target&quot;:&quot;UNDERLINE_NAV.TAB&quot;}" data-view-component="true" class="UnderlineNav-item no-wrap js-responsive-underlinenav-item js-selected-navigation-item">
    
              <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-graph UnderlineNav-octicon d-none d-sm-inline">
    <path d="M1.5 1.75V13.5h13.75a.75.75 0 0 1 0 1.5H.75a.75.75 0 0 1-.75-.75V1.75a.75.75 0 0 1 1.5 0Zm14.28 2.53-5.25 5.25a.75.75 0 0 1-1.06 0L7 7.06 4.28 9.78a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042l3.25-3.25a.75.75 0 0 1 1.06 0L10 7.94l4.72-4.72a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042Z"></path>
</svg>
        <span data-content="Insights">Insights</span>
          <span id="insights-repo-tab-count" data-pjax-replace="" data-turbo-replace="" title="Not available" data-view-component="true" class="Counter"></span>


    
</a></li>
</ul>
    <div style="visibility:hidden;" data-view-component="true" class="UnderlineNav-actions js-responsive-underlinenav-overflow position-absolute pr-3 pr-md-4 pr-lg-5 right-0">      <action-menu data-select-variant="none" data-view-component="true" data-catalyst="">
  <focus-group direction="vertical" mnemonics="" retain="">
    <button id="action-menu-e8f467c4-2b68-49e4-b118-760e2e26d95f-button" popovertarget="action-menu-e8f467c4-2b68-49e4-b118-760e2e26d95f-overlay" aria-controls="action-menu-e8f467c4-2b68-49e4-b118-760e2e26d95f-list" aria-haspopup="true" aria-labelledby="tooltip-6e45e04c-5be7-4665-b3c3-b194ef3caf06" type="button" data-view-component="true" class="Button Button--iconOnly Button--secondary Button--medium UnderlineNav-item">  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-kebab-horizontal Button-visual">
    <path d="M8 9a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3ZM1.5 9a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Zm13 0a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Z"></path>
</svg>
</button><tool-tip id="tooltip-6e45e04c-5be7-4665-b3c3-b194ef3caf06" for="action-menu-e8f467c4-2b68-49e4-b118-760e2e26d95f-button" popover="manual" data-direction="s" data-type="label" data-view-component="true" class="sr-only position-absolute" aria-hidden="true" role="tooltip"><template shadowrootmode="open"><style>
      :host {
        --tooltip-top: var(--tool-tip-position-top, 0);
        --tooltip-left: var(--tool-tip-position-left, 0);
        padding: var(--overlay-paddingBlock-condensed) var(--overlay-padding-condensed) !important;
        font: var(--text-body-shorthand-small);
        color: var(--tooltip-fgColor, var(--fgColor-onEmphasis)) !important;
        text-align: center;
        text-decoration: none;
        text-shadow: none;
        text-transform: none;
        letter-spacing: normal;
        word-wrap: break-word;
        white-space: pre;
        background: var(--tooltip-bgColor, var(--bgColor-emphasis)) !important;
        border-radius: var(--borderRadius-medium);
        border: 0 !important;
        opacity: 0;
        max-width: var(--overlay-width-small);
        word-wrap: break-word;
        white-space: normal;
        width: max-content !important;
        inset: var(--tooltip-top) auto auto var(--tooltip-left) !important;
        overflow: visible !important;
        text-wrap: balance;
      }

      :host(:is(.tooltip-n, .tooltip-nw, .tooltip-ne)) {
        --tooltip-top: calc(var(--tool-tip-position-top, 0) - var(--overlay-offset, 0.25rem));
        --tooltip-left: var(--tool-tip-position-left);
      }

      :host(:is(.tooltip-s, .tooltip-sw, .tooltip-se)) {
        --tooltip-top: calc(var(--tool-tip-position-top, 0) + var(--overlay-offset, 0.25rem));
        --tooltip-left: var(--tool-tip-position-left);
      }

      :host(.tooltip-w) {
        --tooltip-top: var(--tool-tip-position-top);
        --tooltip-left: calc(var(--tool-tip-position-left, 0) - var(--overlay-offset, 0.25rem));
      }

      :host(.tooltip-e) {
        --tooltip-top: var(--tool-tip-position-top);
        --tooltip-left: calc(var(--tool-tip-position-left, 0) + var(--overlay-offset, 0.25rem));
      }

      :host:after{
        position: absolute;
        display: block;
        right: 0;
        left: 0;
        height: var(--overlay-offset, 0.25rem);
        content: "";
      }

      :host(.tooltip-s):after,
      :host(.tooltip-se):after,
      :host(.tooltip-sw):after {
        bottom: 100%
      }

      :host(.tooltip-n):after,
      :host(.tooltip-ne):after,
      :host(.tooltip-nw):after {
        top: 100%;
      }

      @keyframes tooltip-appear {
        from {
          opacity: 0;
        }
        to {
          opacity: 1;
        }
      }

      :host(:popover-open),
      :host(:popover-open):before {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      :host(.\:popover-open) {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      @media (forced-colors: active) {
        :host {
          outline: solid 1px transparent;
        }

        :host:before {
          display: none;
        }
      }
    </style><slot></slot></template>Additional navigation options</tool-tip>


<anchored-position id="action-menu-e8f467c4-2b68-49e4-b118-760e2e26d95f-overlay" anchor="action-menu-e8f467c4-2b68-49e4-b118-760e2e26d95f-button" align="start" side="outside-bottom" anchor-offset="normal" popover="auto" data-view-component="true" style="inset: 36px auto auto 0px;">
  <div data-view-component="true" class="Overlay Overlay--size-auto">
    
      <div data-view-component="true" class="Overlay-body Overlay-body--paddingNone">          <action-list data-catalyst="">
  <div data-view-component="true">
    <ul aria-labelledby="action-menu-e8f467c4-2b68-49e4-b118-760e2e26d95f-button" id="action-menu-e8f467c4-2b68-49e4-b118-760e2e26d95f-list" role="menu" data-view-component="true" class="ActionListWrap--inset ActionListWrap">
        <li hidden="" data-menu-item="i0code-tab" data-targets="action-list.items" role="none" data-view-component="true" class="ActionListItem">
    
    
    <a tabindex="-1" id="item-1c4cea50-1d29-4820-b5d1-e5af8280a51a" href="https://github.com/SumaikaImran/AI_LABS" role="menuitem" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-code">
    <path d="m11.28 3.22 4.25 4.25a.75.75 0 0 1 0 1.06l-4.25 4.25a.749.749 0 0 1-1.275-.326.749.749 0 0 1 .215-.734L13.94 8l-3.72-3.72a.749.749 0 0 1 .326-1.275.749.749 0 0 1 .734.215Zm-6.56 0a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042L2.06 8l3.72 3.72a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L.47 8.53a.75.75 0 0 1 0-1.06Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Code
</span>      
</a>
  
</li>
        <li hidden="" data-menu-item="i1issues-tab" data-targets="action-list.items" role="none" data-view-component="true" class="ActionListItem">
    
    
    <a tabindex="-1" id="item-819c6d44-3822-42c1-9493-55ba17666edb" href="https://github.com/SumaikaImran/AI_LABS/issues" role="menuitem" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-issue-opened">
    <path d="M8 9.5a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Z"></path><path d="M8 0a8 8 0 1 1 0 16A8 8 0 0 1 8 0ZM1.5 8a6.5 6.5 0 1 0 13 0 6.5 6.5 0 0 0-13 0Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Issues
</span>      
</a>
  
</li>
        <li hidden="" data-menu-item="i2pull-requests-tab" data-targets="action-list.items" role="none" data-view-component="true" class="ActionListItem">
    
    
    <a tabindex="-1" id="item-36214194-a4a6-40ff-8a31-51e16e40d175" href="https://github.com/SumaikaImran/AI_LABS/pulls" role="menuitem" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-git-pull-request">
    <path d="M1.5 3.25a2.25 2.25 0 1 1 3 2.122v5.256a2.251 2.251 0 1 1-1.5 0V5.372A2.25 2.25 0 0 1 1.5 3.25Zm5.677-.177L9.573.677A.25.25 0 0 1 10 .854V2.5h1A2.5 2.5 0 0 1 13.5 5v5.628a2.251 2.251 0 1 1-1.5 0V5a1 1 0 0 0-1-1h-1v1.646a.25.25 0 0 1-.427.177L7.177 3.427a.25.25 0 0 1 0-.354ZM3.75 2.5a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5Zm0 9.5a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5Zm8.25.75a.75.75 0 1 0 1.5 0 .75.75 0 0 0-1.5 0Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Pull requests
</span>      
</a>
  
</li>
        <li hidden="" data-menu-item="i3actions-tab" data-targets="action-list.items" role="none" data-view-component="true" class="ActionListItem">
    
    
    <a tabindex="-1" id="item-93d8d68b-c780-452c-af12-b48d69190779" href="https://github.com/SumaikaImran/AI_LABS/actions" role="menuitem" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-play">
    <path d="M8 0a8 8 0 1 1 0 16A8 8 0 0 1 8 0ZM1.5 8a6.5 6.5 0 1 0 13 0 6.5 6.5 0 0 0-13 0Zm4.879-2.773 4.264 2.559a.25.25 0 0 1 0 .428l-4.264 2.559A.25.25 0 0 1 6 10.559V5.442a.25.25 0 0 1 .379-.215Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Actions
</span>      
</a>
  
</li>
        <li hidden="" data-menu-item="i4projects-tab" data-targets="action-list.items" role="none" data-view-component="true" class="ActionListItem">
    
    
    <a tabindex="-1" id="item-a4f20882-e59d-4792-9f67-33808c2067f3" href="https://github.com/SumaikaImran/AI_LABS/projects" role="menuitem" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-table">
    <path d="M0 1.75C0 .784.784 0 1.75 0h12.5C15.216 0 16 .784 16 1.75v12.5A1.75 1.75 0 0 1 14.25 16H1.75A1.75 1.75 0 0 1 0 14.25ZM6.5 6.5v8h7.75a.25.25 0 0 0 .25-.25V6.5Zm8-1.5V1.75a.25.25 0 0 0-.25-.25H6.5V5Zm-13 1.5v7.75c0 .138.112.25.25.25H5v-8ZM5 5V1.5H1.75a.25.25 0 0 0-.25.25V5Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Projects
</span>      
</a>
  
</li>
        <li hidden="" data-menu-item="i5security-tab" data-targets="action-list.items" role="none" data-view-component="true" class="ActionListItem">
    
    
    <a tabindex="-1" id="item-13645cda-a053-4133-830c-48955ee82199" href="https://github.com/SumaikaImran/AI_LABS/security" role="menuitem" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-shield">
    <path d="M7.467.133a1.748 1.748 0 0 1 1.066 0l5.25 1.68A1.75 1.75 0 0 1 15 3.48V7c0 1.566-.32 3.182-1.303 4.682-.983 1.498-2.585 2.813-5.032 3.855a1.697 1.697 0 0 1-1.33 0c-2.447-1.042-4.049-2.357-5.032-3.855C1.32 10.182 1 8.566 1 7V3.48a1.75 1.75 0 0 1 1.217-1.667Zm.61 1.429a.25.25 0 0 0-.153 0l-5.25 1.68a.25.25 0 0 0-.174.238V7c0 1.358.275 2.666 1.057 3.86.784 1.194 2.121 2.34 4.366 3.297a.196.196 0 0 0 .154 0c2.245-.956 3.582-2.104 4.366-3.298C13.225 9.666 13.5 8.36 13.5 7V3.48a.251.251 0 0 0-.174-.237l-5.25-1.68ZM8.75 4.75v3a.75.75 0 0 1-1.5 0v-3a.75.75 0 0 1 1.5 0ZM9 10.5a1 1 0 1 1-2 0 1 1 0 0 1 2 0Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Security
</span>      
</a>
  
</li>
        <li hidden="" data-menu-item="i6insights-tab" data-targets="action-list.items" role="none" data-view-component="true" class="ActionListItem">
    
    
    <a tabindex="-1" id="item-f90f11ba-f2c1-4db9-a736-8598b57a8572" href="https://github.com/SumaikaImran/AI_LABS/pulse" role="menuitem" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-graph">
    <path d="M1.5 1.75V13.5h13.75a.75.75 0 0 1 0 1.5H.75a.75.75 0 0 1-.75-.75V1.75a.75.75 0 0 1 1.5 0Zm14.28 2.53-5.25 5.25a.75.75 0 0 1-1.06 0L7 7.06 4.28 9.78a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042l3.25-3.25a.75.75 0 0 1 1.06 0L10 7.94l4.72-4.72a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Insights
</span>      
</a>
  
</li>
</ul>    
</div></action-list>


</div>
      
</div></anchored-position>  </focus-group>
</action-menu></div>
</nav>
      </div>
</header>


      <div hidden="hidden" data-view-component="true" class="js-stale-session-flash stale-session-flash flash flash-warn flash-full">
  
        <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-alert">
    <path d="M6.457 1.047c.659-1.234 2.427-1.234 3.086 0l6.082 11.378A1.75 1.75 0 0 1 14.082 15H1.918a1.75 1.75 0 0 1-1.543-2.575Zm1.763.707a.25.25 0 0 0-.44 0L1.698 13.132a.25.25 0 0 0 .22.368h12.164a.25.25 0 0 0 .22-.368Zm.53 3.996v2.5a.75.75 0 0 1-1.5 0v-2.5a.75.75 0 0 1 1.5 0ZM9 11a1 1 0 1 1-2 0 1 1 0 0 1 2 0Z"></path>
</svg>
        <span class="js-stale-session-flash-signed-in" hidden="">You signed in with another tab or window. <a class="Link--inTextBlock" href="https://github.com/SumaikaImran/AI_LABS/blob/main/app.py">Reload</a> to refresh your session.</span>
        <span class="js-stale-session-flash-signed-out" hidden="">You signed out in another tab or window. <a class="Link--inTextBlock" href="https://github.com/SumaikaImran/AI_LABS/blob/main/app.py">Reload</a> to refresh your session.</span>
        <span class="js-stale-session-flash-switched" hidden="">You switched accounts on another tab or window. <a class="Link--inTextBlock" href="https://github.com/SumaikaImran/AI_LABS/blob/main/app.py">Reload</a> to refresh your session.</span>

    <button id="icon-button-b6b6fac8-66d9-4d79-8fc7-bbe1ccf985e4" aria-labelledby="tooltip-2bfcf8c6-951a-4f5c-b9d0-1f6c7ee24995" type="button" data-view-component="true" class="Button Button--iconOnly Button--invisible Button--medium flash-close js-flash-close">  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-x Button-visual">
    <path d="M3.72 3.72a.75.75 0 0 1 1.06 0L8 6.94l3.22-3.22a.749.749 0 0 1 1.275.326.749.749 0 0 1-.215.734L9.06 8l3.22 3.22a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L8 9.06l-3.22 3.22a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042L6.94 8 3.72 4.78a.75.75 0 0 1 0-1.06Z"></path>
</svg>
</button><tool-tip id="tooltip-2bfcf8c6-951a-4f5c-b9d0-1f6c7ee24995" for="icon-button-b6b6fac8-66d9-4d79-8fc7-bbe1ccf985e4" popover="manual" data-direction="s" data-type="label" data-view-component="true" class="sr-only position-absolute" aria-hidden="true" role="tooltip"><template shadowrootmode="open"><style>
      :host {
        --tooltip-top: var(--tool-tip-position-top, 0);
        --tooltip-left: var(--tool-tip-position-left, 0);
        padding: var(--overlay-paddingBlock-condensed) var(--overlay-padding-condensed) !important;
        font: var(--text-body-shorthand-small);
        color: var(--tooltip-fgColor, var(--fgColor-onEmphasis)) !important;
        text-align: center;
        text-decoration: none;
        text-shadow: none;
        text-transform: none;
        letter-spacing: normal;
        word-wrap: break-word;
        white-space: pre;
        background: var(--tooltip-bgColor, var(--bgColor-emphasis)) !important;
        border-radius: var(--borderRadius-medium);
        border: 0 !important;
        opacity: 0;
        max-width: var(--overlay-width-small);
        word-wrap: break-word;
        white-space: normal;
        width: max-content !important;
        inset: var(--tooltip-top) auto auto var(--tooltip-left) !important;
        overflow: visible !important;
        text-wrap: balance;
      }

      :host(:is(.tooltip-n, .tooltip-nw, .tooltip-ne)) {
        --tooltip-top: calc(var(--tool-tip-position-top, 0) - var(--overlay-offset, 0.25rem));
        --tooltip-left: var(--tool-tip-position-left);
      }

      :host(:is(.tooltip-s, .tooltip-sw, .tooltip-se)) {
        --tooltip-top: calc(var(--tool-tip-position-top, 0) + var(--overlay-offset, 0.25rem));
        --tooltip-left: var(--tool-tip-position-left);
      }

      :host(.tooltip-w) {
        --tooltip-top: var(--tool-tip-position-top);
        --tooltip-left: calc(var(--tool-tip-position-left, 0) - var(--overlay-offset, 0.25rem));
      }

      :host(.tooltip-e) {
        --tooltip-top: var(--tool-tip-position-top);
        --tooltip-left: calc(var(--tool-tip-position-left, 0) + var(--overlay-offset, 0.25rem));
      }

      :host:after{
        position: absolute;
        display: block;
        right: 0;
        left: 0;
        height: var(--overlay-offset, 0.25rem);
        content: "";
      }

      :host(.tooltip-s):after,
      :host(.tooltip-se):after,
      :host(.tooltip-sw):after {
        bottom: 100%
      }

      :host(.tooltip-n):after,
      :host(.tooltip-ne):after,
      :host(.tooltip-nw):after {
        top: 100%;
      }

      @keyframes tooltip-appear {
        from {
          opacity: 0;
        }
        to {
          opacity: 1;
        }
      }

      :host(:popover-open),
      :host(:popover-open):before {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      :host(.\:popover-open) {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      @media (forced-colors: active) {
        :host {
          outline: solid 1px transparent;
        }

        :host:before {
          display: none;
        }
      }
    </style><slot></slot></template>Dismiss alert</tool-tip>


  
</div>
          
    </div>

  <div id="start-of-content" class="show-on-focus"></div>








    <div id="js-flash-container" class="flash-container" data-turbo-replace="">




  <template class="js-flash-template"></template>
</div>


    
  <notification-shelf-watcher data-base-url="https://github.com/notifications/beta/shelf" data-channel="eyJjIjoibm90aWZpY2F0aW9uLWNoYW5nZWQ6MTQ2MDYzODE0IiwidCI6MTczMjg1MjM2Nn0=--0c140f91799b8d1f7240cfdbf4c7318c480adc1d33f3bb8aca8388b183389a06" data-view-component="true" class="js-socket-channel" data-refresh-delay="500" data-catalyst="" data-throttle-delay="5000"></notification-shelf-watcher>
  <div hidden="" data-initial="" data-target="notification-shelf-watcher.placeholder"></div>






  <div class="application-main " data-commit-hovercards-enabled="" data-discussion-hovercards-enabled="" data-issue-and-pr-hovercards-enabled="">
        <div itemscope="" itemtype="http://schema.org/SoftwareSourceCode" class="">
    <main id="js-repo-pjax-container">
      
      






    
  <div id="repository-container-header" data-turbo-replace="" hidden=""></div>




<turbo-frame id="repo-content-turbo-frame" target="_top" data-turbo-action="advance" class="">
    <div id="repo-content-pjax-container" class="repository-content ">
      <a href="https://github.dev/" class="d-none js-github-dev-shortcut" data-hotkey=".,Mod+Alt+.">Open in github.dev</a>
  <a href="https://github.dev/" class="d-none js-github-dev-new-tab-shortcut" data-hotkey="Shift+.,Shift+&gt;,&gt;" target="_blank" rel="noopener noreferrer">Open in a new github.dev tab</a>
    <a class="d-none" data-hotkey=",,Mod+Alt+," target="_blank" href="https://github.com/codespaces/new/SumaikaImran/AI_LABS/tree/main?resume=1">Open in codespace</a>




    
      
    








<react-app app-name="react-code-view" initial-path="/SumaikaImran/AI_LABS/blob/main/app.py" class="react-app loaded" data-attempted-ssr="true" data-ssr="true" data-lazy="false" data-alternate="false" data-catalyst="">
  
  <script type="application/json" data-target="react-app.embeddedData">{"payload":{"allShortcutsEnabled":true,"fileTree":{"":{"items":[{"name":"IDS.py","path":"IDS.py","contentType":"file"},{"name":"ai lab8_9.pdf","path":"ai lab8_9.pdf","contentType":"file"},{"name":"app.py","path":"app.py","contentType":"file"}],"totalCount":3}},"fileTreeProcessingTime":42.378659,"foldersToFetch":[],"repo":{"id":871997669,"defaultBranch":"main","name":"AI_LABS","ownerLogin":"SumaikaImran","currentUserCanPush":false,"isFork":false,"isEmpty":false,"createdAt":"2024-10-13T19:22:26.000+05:00","ownerAvatar":"https://avatars.githubusercontent.com/u/147117851?v=4","public":true,"private":false,"isOrgOwned":false},"codeLineWrapEnabled":false,"symbolsExpanded":true,"treeExpanded":true,"refInfo":{"name":"main","listCacheKey":"v0:1728829455.0","canEdit":true,"refType":"branch","currentOid":"eb24e56c25aa1eb1b2b3deb15eec180a82da33ad"},"path":"app.py","currentUser":{"id":146063814,"login":"Malaika-Mustafa","userEmail":"malaikamustafa662@gmail.com"},"blob":{"rawLines":["\r","from flask import Flask, render_template, request\r","\r","app = Flask(__name__)\r","\r","# Route for the main page\r","@app.route('/')\r","def index():\r","    return render_template('index.html')\r","\r","# Route to generate a surgery schedule based on input\r","@app.route('/generate_schedule', methods=['POST'])\r","def generate_schedule():\r","    try:\r","        # Get the input values from the form\r","        num_surgeries = int(request.form['num_surgeries'])\r","        num_rooms = int(request.form['num_rooms'])\r","        num_staff = int(request.form['num_staff'])\r","\r","        # Get the durations of each surgery\r","        durations = [int(request.form[f'duration_{i+1}']) for i in range(num_surgeries)]\r","\r","        # Get staff skills for each surgery\r","        staff_skills = []\r","        for i in range(num_surgeries):\r","            skills = [\r","                int(request.form.get(f'surgery_{i+1}_staff_{j+1}', 0)) \r","                for j in range(1, num_staff + 1)\r","            ] \r","            '''request.forms.get Retrieves the value of the form input corresponding to whether staff member j is available for surgery i+1.\r","Example: If i = 0 (first surgery) and j = 1 (first staff member), it looks for the input field with the name surgery_1_staff_1.\r","The default value is 0, meaning if the input is missing, it assumes that the staff member is unavailable for that surgery.'''\r","#Collect the skills (binary values: 0 or 1) of all staff members for the current surgery\r","            staff_skills.append(skills)\r","            '''skills is a list Each row corresponds to a surgery.\r","Each element in a row is 0 or 1, indicating whether a specific staff member is available for that surgery.'''\r","\r","        # Generate the schedule using the genetic algorithm\r","        schedule = genetic_algorithm(num_surgeries, num_rooms, num_staff, durations, staff_skills)\r","\r"," \r","        \"\"\"\r","            If no valid schedule is generated, display an error message.\r","             This may occur if inputs are inconsistent or constraints cannot be satisfied.\r","             \"\"\"\r","        if not schedule:\r","            error = \"No valid schedule could be generated. Please check the inputs and try again.\"\r","            return render_template('index.html', error=error)\r","        \r","        # Render the schedule on the page\r","        return render_template('index.html', schedule=schedule)\r","\r","    except Exception as e:\r","        # Handle errors gracefully and display the error message\r","        return render_template('index.html', error=f\"An error occurred: {e}\")\r","\r","# Genetic Algorithm for generating an optimal surgery schedule\r","def genetic_algorithm(num_surgeries, num_rooms, num_staff, durations, staff_skills, slot_duration=40, max_room_slots=7):\r","    import random\r","# Genetic Algorithm to generate an optimal schedule for surgeries.\r","    \r","#     Parameters:\r","#         num_surgeries (int): Total number of surgeries to schedule.\r","#         num_rooms (int): Number of available operating rooms.\r","#         num_staff (int): Total staff members available.\r","#         durations (list): List of surgery durations.\r","#         staff_skills (list): 2D list indicating staff eligibility for each surgery.\r","#         slot_duration (int): Duration of each time slot in minutes (default: 40).\r","#         max_room_slots (int): Maximum time slots available per room (default: 7).\r","    # Calculate the number of slots required for each surgery\r","    # (divide surgery duration by slot duration, rounding up for partial slots)\r","   # Returns:\r","#         list: A schedule containing surgery details or None if no valid schedule is found.\r","    slots_required = [(-(-dur // slot_duration)) for dur in durations] \r","    \r","    #to perform ceiling division using integer arithmetic\r","    '''Floor division (//) truncates toward zero, while ceiling division needs to round up.\r","Negating the number \"reverses\" the truncation direction of //, effectively performing a ceiling operation.(-(-50 // 40))  # Perform step by step\r","= -((-50) // 40)\r","= -(-2)  # -50 divided by 40 is -1.25, floored to -2\r","= 2  '''\r","\r","    # Validate staff availability for each surgery\r","    valid_staff = []\r","    for i in range(num_surgeries):\r","        \"\"\"\r","       Collect a list of staff members eligible for each surgery.\r","         If no staff is available for a surgery, return None to indicate an invalid schedule.\r","         \"\"\"\r","        staff_for_surgery = [s + 1 for s, can_do in enumerate(staff_skills[i]) ]\r","        if not staff_for_surgery:\r","            return None  # If no staff is available for a surgery, return an invalid schedule\r","        valid_staff.append(staff_for_surgery)\r","\r","    # Step 1: Initialize the population with random schedules\r","    population = []\r","    for _ in range(50):  # Population size of 50\r","        \"\"\"\r","       Create a random schedule for each individual in the population.\r","         Assign surgeries to random rooms, time slots, and eligible staff members.\r","         \"\"\"\r","        individual = []\r","        for i in range(num_surgeries):\r","            room = random.randint(1, num_rooms)  # Assign a random room\r","            start_slot = random.randint(1, max_room_slots - slots_required[i] + 1)  # Assign a random starting slot\r","            assigned_staff = random.sample(valid_staff[i], k=1)  # Randomly assign at least one valid staff member\r","            individual.append({\r","                \"surgery\": i + 1, \r","                \"room\": room,  # Assigned room\r","                \"start_slot\": start_slot,  # Starting time slot\r","                \"end_slot\": start_slot + slots_required[i] - 1,  # Ending time slot\r","                \"staff\": assigned_staff  # Assigned staff members\r","            })\r","        population.append(individual)\r","\r","    # Fitness Function: Evaluate the quality of a schedule\r","    def fitness(individual):\r","\r","        \"\"\"\r","        Calculate the fitness of a schedule.\r","        \r","        Parameters:\r","            individual (list): A schedule (list of surgeries with room, time slot, and staff assignments).\r","        \r","        Returns:\r","            int: A fitness score based on overlap and staff assignment validity.\r","        \"\"\"\r","        score = 0\r","        room_schedule = {room: [] for room in range(1, num_rooms + 1)}  # Track room schedules\r","\r","        for surgery in individual:\r","            room = surgery[\"room\"]\r","            start = surgery[\"start_slot\"]\r","            end = surgery[\"end_slot\"]\r","\r","            # Penalize overlapping surgeries in the same room\r","            for booked in room_schedule[room]:\r","                if not (end \u003c booked[0] or start \u003e booked[1]):  # Overlap detected\r","                    score -= 10\r","\r","            # Penalize invalid staff assignments\r","            for staff in surgery[\"staff\"]:\r","                if staff not in valid_staff[surgery[\"surgery\"] - 1]:\r","                    score -= 1   #changed from 15\r","\r","            # Update the room's schedule\r","            room_schedule[room].append((start, end))\r","            score += 1  # Reward valid room and staff assignments changed from 5 to 1\r","\r","        return score\r","\r","    # Evolution Function: Create the next generation of schedules\r","    def evolve(population):\r","        \r","        # Sort the population by fitness (higher is better)\r","        population.sort(key=lambda x: fitness(x), reverse=True)\r","\r","        # Select the top 10 schedules as parents for the next generation\r","        new_population = population[:10]\r","\r","        # Generate new individuals by crossover and mutation until the population is full\r","        while len(new_population) \u003c 50:\r","            # Select two parents from the top 10 fittest schedules\r","            p1, p2 = random.sample(population[:10], 2)\r","\r","            # Perform crossover by combining parts of the parents\r","            crossover_point = random.randint(0, num_surgeries - 1)\r","            child = p1[:crossover_point] + p2[crossover_point:]\r","\r","            # Mutation: Randomly adjust room or starting slot for some surgeries\r","            if random.random() \u003c 0.01:  # 1% chance of mutation\r","                idx = random.randint(0, num_surgeries - 1)  # Select a random surgery to mutate\r","                child[idx][\"room\"] = random.randint(1, num_rooms)  # Assign a new random room\r","                child[idx][\"start_slot\"] = random.randint(1, max_room_slots - slots_required[idx] + 1)  # Assign a new random start slot\r","\r","            # Add the mutated child to the new population\r","            new_population.append(child)\r","\r","        return new_population\r","\r","    # Step 2: Run the genetic algorithm for a fixed number of generations\r","    for _ in range(50):  # Run for 50 generations\r","        population = evolve(population)  # Evolve the population\r","\r","    # Step 3: Select the best schedule from the final generation\r","    best_schedule = max(population, key=lambda x: fitness(x))\r","\r","    # Format the best schedule for display\r","    final_schedule = []\r","    for surgery in best_schedule:\r","        final_schedule.append({\r","            \"surgery\": surgery[\"surgery\"],\r","            \"room\": surgery[\"room\"],\r","            \"slots\": f\"{surgery['start_slot']} - {surgery['end_slot']}\",\r","            \"staff\": ', '.join(map(str, surgery[\"staff\"])) if surgery[\"staff\"] else \"No Staff Assigned\"\r","        })\r","\r","    return final_schedule\r","\r","# Run the Flask app\r","if __name__ == '__main__':\r","    app.run(debug=True)\r","\r","\r","\r","\r","        "],"stylingDirectives":[[],[{"s":0,"e":4,"c":"pl-k"},{"s":5,"e":10,"c":"pl-s1"},{"s":11,"e":17,"c":"pl-k"},{"s":18,"e":23,"c":"pl-v"},{"s":25,"e":40,"c":"pl-s1"},{"s":42,"e":49,"c":"pl-s1"}],[],[{"s":0,"e":3,"c":"pl-s1"},{"s":4,"e":5,"c":"pl-c1"},{"s":6,"e":11,"c":"pl-v"},{"s":12,"e":20,"c":"pl-s1"}],[],[{"s":0,"e":26,"c":"pl-c"}],[{"s":0,"e":15,"c":"pl-en"},{"s":1,"e":4,"c":"pl-s1"},{"s":5,"e":10,"c":"pl-en"},{"s":11,"e":14,"c":"pl-s"}],[{"s":0,"e":3,"c":"pl-k"},{"s":4,"e":9,"c":"pl-en"}],[{"s":4,"e":10,"c":"pl-k"},{"s":11,"e":26,"c":"pl-en"},{"s":27,"e":39,"c":"pl-s"}],[],[{"s":0,"e":54,"c":"pl-c"}],[{"s":0,"e":50,"c":"pl-en"},{"s":1,"e":4,"c":"pl-s1"},{"s":5,"e":10,"c":"pl-en"},{"s":11,"e":31,"c":"pl-s"},{"s":33,"e":40,"c":"pl-s1"},{"s":40,"e":41,"c":"pl-c1"},{"s":42,"e":48,"c":"pl-s"}],[{"s":0,"e":3,"c":"pl-k"},{"s":4,"e":21,"c":"pl-en"}],[{"s":4,"e":7,"c":"pl-k"}],[{"s":8,"e":45,"c":"pl-c"}],[{"s":8,"e":21,"c":"pl-s1"},{"s":22,"e":23,"c":"pl-c1"},{"s":24,"e":27,"c":"pl-en"},{"s":28,"e":35,"c":"pl-s1"},{"s":36,"e":40,"c":"pl-s1"},{"s":41,"e":56,"c":"pl-s"}],[{"s":8,"e":17,"c":"pl-s1"},{"s":18,"e":19,"c":"pl-c1"},{"s":20,"e":23,"c":"pl-en"},{"s":24,"e":31,"c":"pl-s1"},{"s":32,"e":36,"c":"pl-s1"},{"s":37,"e":48,"c":"pl-s"}],[{"s":8,"e":17,"c":"pl-s1"},{"s":18,"e":19,"c":"pl-c1"},{"s":20,"e":23,"c":"pl-en"},{"s":24,"e":31,"c":"pl-s1"},{"s":32,"e":36,"c":"pl-s1"},{"s":37,"e":48,"c":"pl-s"}],[],[{"s":8,"e":44,"c":"pl-c"}],[{"s":8,"e":17,"c":"pl-s1"},{"s":18,"e":19,"c":"pl-c1"},{"s":21,"e":24,"c":"pl-en"},{"s":25,"e":32,"c":"pl-s1"},{"s":33,"e":37,"c":"pl-s1"},{"s":38,"e":55,"c":"pl-s"},{"s":49,"e":54,"c":"pl-s1"},{"s":49,"e":50,"c":"pl-kos"},{"s":50,"e":51,"c":"pl-s1"},{"s":51,"e":52,"c":"pl-c1"},{"s":52,"e":53,"c":"pl-c1"},{"s":53,"e":54,"c":"pl-kos"},{"s":58,"e":61,"c":"pl-k"},{"s":62,"e":63,"c":"pl-s1"},{"s":64,"e":66,"c":"pl-c1"},{"s":67,"e":72,"c":"pl-en"},{"s":73,"e":86,"c":"pl-s1"}],[],[{"s":8,"e":44,"c":"pl-c"}],[{"s":8,"e":20,"c":"pl-s1"},{"s":21,"e":22,"c":"pl-c1"}],[{"s":8,"e":11,"c":"pl-k"},{"s":12,"e":13,"c":"pl-s1"},{"s":14,"e":16,"c":"pl-c1"},{"s":17,"e":22,"c":"pl-en"},{"s":23,"e":36,"c":"pl-s1"}],[{"s":12,"e":18,"c":"pl-s1"},{"s":19,"e":20,"c":"pl-c1"}],[{"s":16,"e":19,"c":"pl-en"},{"s":20,"e":27,"c":"pl-s1"},{"s":28,"e":32,"c":"pl-s1"},{"s":33,"e":36,"c":"pl-en"},{"s":37,"e":65,"c":"pl-s"},{"s":47,"e":52,"c":"pl-s1"},{"s":47,"e":48,"c":"pl-kos"},{"s":48,"e":49,"c":"pl-s1"},{"s":49,"e":50,"c":"pl-c1"},{"s":50,"e":51,"c":"pl-c1"},{"s":51,"e":52,"c":"pl-kos"},{"s":59,"e":64,"c":"pl-s1"},{"s":59,"e":60,"c":"pl-kos"},{"s":60,"e":61,"c":"pl-s1"},{"s":61,"e":62,"c":"pl-c1"},{"s":62,"e":63,"c":"pl-c1"},{"s":63,"e":64,"c":"pl-kos"},{"s":67,"e":68,"c":"pl-c1"}],[{"s":16,"e":19,"c":"pl-k"},{"s":20,"e":21,"c":"pl-s1"},{"s":22,"e":24,"c":"pl-c1"},{"s":25,"e":30,"c":"pl-en"},{"s":31,"e":32,"c":"pl-c1"},{"s":34,"e":43,"c":"pl-s1"},{"s":44,"e":45,"c":"pl-c1"},{"s":46,"e":47,"c":"pl-c1"}],[],[{"s":12,"e":141,"c":"pl-s"}],[{"s":0,"e":128,"c":"pl-s"}],[{"s":0,"e":125,"c":"pl-s"}],[{"s":0,"e":89,"c":"pl-c"}],[{"s":12,"e":24,"c":"pl-s1"},{"s":25,"e":31,"c":"pl-en"},{"s":32,"e":38,"c":"pl-s1"}],[{"s":12,"e":67,"c":"pl-s"}],[{"s":0,"e":109,"c":"pl-s"}],[],[{"s":8,"e":60,"c":"pl-c"}],[{"s":8,"e":16,"c":"pl-s1"},{"s":17,"e":18,"c":"pl-c1"},{"s":19,"e":36,"c":"pl-en"},{"s":37,"e":50,"c":"pl-s1"},{"s":52,"e":61,"c":"pl-s1"},{"s":63,"e":72,"c":"pl-s1"},{"s":74,"e":83,"c":"pl-s1"},{"s":85,"e":97,"c":"pl-s1"}],[],[],[{"s":8,"e":12,"c":"pl-s"}],[{"s":0,"e":73,"c":"pl-s"}],[{"s":0,"e":91,"c":"pl-s"}],[{"s":0,"e":16,"c":"pl-s"}],[{"s":8,"e":10,"c":"pl-k"},{"s":11,"e":14,"c":"pl-c1"},{"s":15,"e":23,"c":"pl-s1"}],[{"s":12,"e":17,"c":"pl-s1"},{"s":18,"e":19,"c":"pl-c1"},{"s":20,"e":98,"c":"pl-s"}],[{"s":12,"e":18,"c":"pl-k"},{"s":19,"e":34,"c":"pl-en"},{"s":35,"e":47,"c":"pl-s"},{"s":49,"e":54,"c":"pl-s1"},{"s":54,"e":55,"c":"pl-c1"},{"s":55,"e":60,"c":"pl-s1"}],[],[{"s":8,"e":42,"c":"pl-c"}],[{"s":8,"e":14,"c":"pl-k"},{"s":15,"e":30,"c":"pl-en"},{"s":31,"e":43,"c":"pl-s"},{"s":45,"e":53,"c":"pl-s1"},{"s":53,"e":54,"c":"pl-c1"},{"s":54,"e":62,"c":"pl-s1"}],[],[{"s":4,"e":10,"c":"pl-k"},{"s":11,"e":20,"c":"pl-v"},{"s":21,"e":23,"c":"pl-k"},{"s":24,"e":25,"c":"pl-s1"}],[{"s":8,"e":65,"c":"pl-c"}],[{"s":8,"e":14,"c":"pl-k"},{"s":15,"e":30,"c":"pl-en"},{"s":31,"e":43,"c":"pl-s"},{"s":45,"e":50,"c":"pl-s1"},{"s":50,"e":51,"c":"pl-c1"},{"s":51,"e":76,"c":"pl-s"},{"s":72,"e":75,"c":"pl-s1"},{"s":72,"e":73,"c":"pl-kos"},{"s":73,"e":74,"c":"pl-s1"},{"s":74,"e":75,"c":"pl-kos"}],[],[{"s":0,"e":63,"c":"pl-c"}],[{"s":0,"e":3,"c":"pl-k"},{"s":4,"e":21,"c":"pl-en"},{"s":22,"e":35,"c":"pl-s1"},{"s":37,"e":46,"c":"pl-s1"},{"s":48,"e":57,"c":"pl-s1"},{"s":59,"e":68,"c":"pl-s1"},{"s":70,"e":82,"c":"pl-s1"},{"s":84,"e":97,"c":"pl-s1"},{"s":97,"e":98,"c":"pl-c1"},{"s":98,"e":100,"c":"pl-c1"},{"s":102,"e":116,"c":"pl-s1"},{"s":116,"e":117,"c":"pl-c1"},{"s":117,"e":118,"c":"pl-c1"}],[{"s":4,"e":10,"c":"pl-k"},{"s":11,"e":17,"c":"pl-s1"}],[{"s":0,"e":67,"c":"pl-c"}],[],[{"s":0,"e":18,"c":"pl-c"}],[{"s":0,"e":70,"c":"pl-c"}],[{"s":0,"e":64,"c":"pl-c"}],[{"s":0,"e":58,"c":"pl-c"}],[{"s":0,"e":55,"c":"pl-c"}],[{"s":0,"e":86,"c":"pl-c"}],[{"s":0,"e":84,"c":"pl-c"}],[{"s":0,"e":84,"c":"pl-c"}],[{"s":4,"e":62,"c":"pl-c"}],[{"s":4,"e":80,"c":"pl-c"}],[{"s":3,"e":14,"c":"pl-c"}],[{"s":0,"e":93,"c":"pl-c"}],[{"s":4,"e":18,"c":"pl-s1"},{"s":19,"e":20,"c":"pl-c1"},{"s":23,"e":24,"c":"pl-c1"},{"s":25,"e":26,"c":"pl-c1"},{"s":26,"e":29,"c":"pl-s1"},{"s":30,"e":32,"c":"pl-c1"},{"s":33,"e":46,"c":"pl-s1"},{"s":49,"e":52,"c":"pl-k"},{"s":53,"e":56,"c":"pl-s1"},{"s":57,"e":59,"c":"pl-c1"},{"s":60,"e":69,"c":"pl-s1"}],[],[{"s":4,"e":58,"c":"pl-c"}],[{"s":4,"e":92,"c":"pl-s"}],[{"s":0,"e":145,"c":"pl-s"}],[{"s":0,"e":17,"c":"pl-s"}],[{"s":0,"e":53,"c":"pl-s"}],[{"s":0,"e":8,"c":"pl-s"}],[],[{"s":4,"e":51,"c":"pl-c"}],[{"s":4,"e":15,"c":"pl-s1"},{"s":16,"e":17,"c":"pl-c1"}],[{"s":4,"e":7,"c":"pl-k"},{"s":8,"e":9,"c":"pl-s1"},{"s":10,"e":12,"c":"pl-c1"},{"s":13,"e":18,"c":"pl-en"},{"s":19,"e":32,"c":"pl-s1"}],[{"s":8,"e":12,"c":"pl-s"}],[{"s":0,"e":66,"c":"pl-s"}],[{"s":0,"e":94,"c":"pl-s"}],[{"s":0,"e":12,"c":"pl-s"}],[{"s":8,"e":25,"c":"pl-s1"},{"s":26,"e":27,"c":"pl-c1"},{"s":29,"e":30,"c":"pl-s1"},{"s":31,"e":32,"c":"pl-c1"},{"s":33,"e":34,"c":"pl-c1"},{"s":35,"e":38,"c":"pl-k"},{"s":39,"e":40,"c":"pl-s1"},{"s":42,"e":48,"c":"pl-s1"},{"s":49,"e":51,"c":"pl-c1"},{"s":52,"e":61,"c":"pl-en"},{"s":62,"e":74,"c":"pl-s1"},{"s":75,"e":76,"c":"pl-s1"}],[{"s":8,"e":10,"c":"pl-k"},{"s":11,"e":14,"c":"pl-c1"},{"s":15,"e":32,"c":"pl-s1"}],[{"s":12,"e":18,"c":"pl-k"},{"s":19,"e":23,"c":"pl-c1"},{"s":25,"e":94,"c":"pl-c"}],[{"s":8,"e":19,"c":"pl-s1"},{"s":20,"e":26,"c":"pl-en"},{"s":27,"e":44,"c":"pl-s1"}],[],[{"s":4,"e":62,"c":"pl-c"}],[{"s":4,"e":14,"c":"pl-s1"},{"s":15,"e":16,"c":"pl-c1"}],[{"s":4,"e":7,"c":"pl-k"},{"s":8,"e":9,"c":"pl-s1"},{"s":10,"e":12,"c":"pl-c1"},{"s":13,"e":18,"c":"pl-en"},{"s":19,"e":21,"c":"pl-c1"},{"s":25,"e":49,"c":"pl-c"}],[{"s":8,"e":12,"c":"pl-s"}],[{"s":0,"e":71,"c":"pl-s"}],[{"s":0,"e":83,"c":"pl-s"}],[{"s":0,"e":12,"c":"pl-s"}],[{"s":8,"e":18,"c":"pl-s1"},{"s":19,"e":20,"c":"pl-c1"}],[{"s":8,"e":11,"c":"pl-k"},{"s":12,"e":13,"c":"pl-s1"},{"s":14,"e":16,"c":"pl-c1"},{"s":17,"e":22,"c":"pl-en"},{"s":23,"e":36,"c":"pl-s1"}],[{"s":12,"e":16,"c":"pl-s1"},{"s":17,"e":18,"c":"pl-c1"},{"s":19,"e":25,"c":"pl-s1"},{"s":26,"e":33,"c":"pl-en"},{"s":34,"e":35,"c":"pl-c1"},{"s":37,"e":46,"c":"pl-s1"},{"s":49,"e":72,"c":"pl-c"}],[{"s":12,"e":22,"c":"pl-s1"},{"s":23,"e":24,"c":"pl-c1"},{"s":25,"e":31,"c":"pl-s1"},{"s":32,"e":39,"c":"pl-en"},{"s":40,"e":41,"c":"pl-c1"},{"s":43,"e":57,"c":"pl-s1"},{"s":58,"e":59,"c":"pl-c1"},{"s":60,"e":74,"c":"pl-s1"},{"s":75,"e":76,"c":"pl-s1"},{"s":78,"e":79,"c":"pl-c1"},{"s":80,"e":81,"c":"pl-c1"},{"s":84,"e":116,"c":"pl-c"}],[{"s":12,"e":26,"c":"pl-s1"},{"s":27,"e":28,"c":"pl-c1"},{"s":29,"e":35,"c":"pl-s1"},{"s":36,"e":42,"c":"pl-en"},{"s":43,"e":54,"c":"pl-s1"},{"s":55,"e":56,"c":"pl-s1"},{"s":59,"e":60,"c":"pl-s1"},{"s":60,"e":61,"c":"pl-c1"},{"s":61,"e":62,"c":"pl-c1"},{"s":65,"e":115,"c":"pl-c"}],[{"s":12,"e":22,"c":"pl-s1"},{"s":23,"e":29,"c":"pl-en"}],[{"s":16,"e":25,"c":"pl-s"},{"s":27,"e":28,"c":"pl-s1"},{"s":29,"e":30,"c":"pl-c1"},{"s":31,"e":32,"c":"pl-c1"}],[{"s":16,"e":22,"c":"pl-s"},{"s":24,"e":28,"c":"pl-s1"},{"s":31,"e":47,"c":"pl-c"}],[{"s":16,"e":28,"c":"pl-s"},{"s":30,"e":40,"c":"pl-s1"},{"s":43,"e":64,"c":"pl-c"}],[{"s":16,"e":26,"c":"pl-s"},{"s":28,"e":38,"c":"pl-s1"},{"s":39,"e":40,"c":"pl-c1"},{"s":41,"e":55,"c":"pl-s1"},{"s":56,"e":57,"c":"pl-s1"},{"s":59,"e":60,"c":"pl-c1"},{"s":61,"e":62,"c":"pl-c1"},{"s":65,"e":84,"c":"pl-c"}],[{"s":16,"e":23,"c":"pl-s"},{"s":25,"e":39,"c":"pl-s1"},{"s":41,"e":66,"c":"pl-c"}],[],[{"s":8,"e":18,"c":"pl-s1"},{"s":19,"e":25,"c":"pl-en"},{"s":26,"e":36,"c":"pl-s1"}],[],[{"s":4,"e":59,"c":"pl-c"}],[{"s":4,"e":7,"c":"pl-k"},{"s":8,"e":15,"c":"pl-en"},{"s":16,"e":26,"c":"pl-s1"}],[],[{"s":8,"e":12,"c":"pl-s"}],[{"s":0,"e":45,"c":"pl-s"}],[{"s":0,"e":9,"c":"pl-s"}],[{"s":0,"e":20,"c":"pl-s"}],[{"s":0,"e":107,"c":"pl-s"}],[{"s":0,"e":9,"c":"pl-s"}],[{"s":0,"e":17,"c":"pl-s"}],[{"s":0,"e":81,"c":"pl-s"}],[{"s":0,"e":11,"c":"pl-s"}],[{"s":8,"e":13,"c":"pl-s1"},{"s":14,"e":15,"c":"pl-c1"},{"s":16,"e":17,"c":"pl-c1"}],[{"s":8,"e":21,"c":"pl-s1"},{"s":22,"e":23,"c":"pl-c1"},{"s":25,"e":29,"c":"pl-s1"},{"s":34,"e":37,"c":"pl-k"},{"s":38,"e":42,"c":"pl-s1"},{"s":43,"e":45,"c":"pl-c1"},{"s":46,"e":51,"c":"pl-en"},{"s":52,"e":53,"c":"pl-c1"},{"s":55,"e":64,"c":"pl-s1"},{"s":65,"e":66,"c":"pl-c1"},{"s":67,"e":68,"c":"pl-c1"},{"s":72,"e":95,"c":"pl-c"}],[],[{"s":8,"e":11,"c":"pl-k"},{"s":12,"e":19,"c":"pl-s1"},{"s":20,"e":22,"c":"pl-c1"},{"s":23,"e":33,"c":"pl-s1"}],[{"s":12,"e":16,"c":"pl-s1"},{"s":17,"e":18,"c":"pl-c1"},{"s":19,"e":26,"c":"pl-s1"},{"s":27,"e":33,"c":"pl-s"}],[{"s":12,"e":17,"c":"pl-s1"},{"s":18,"e":19,"c":"pl-c1"},{"s":20,"e":27,"c":"pl-s1"},{"s":28,"e":40,"c":"pl-s"}],[{"s":12,"e":15,"c":"pl-s1"},{"s":16,"e":17,"c":"pl-c1"},{"s":18,"e":25,"c":"pl-s1"},{"s":26,"e":36,"c":"pl-s"}],[],[{"s":12,"e":62,"c":"pl-c"}],[{"s":12,"e":15,"c":"pl-k"},{"s":16,"e":22,"c":"pl-s1"},{"s":23,"e":25,"c":"pl-c1"},{"s":26,"e":39,"c":"pl-s1"},{"s":40,"e":44,"c":"pl-s1"}],[{"s":16,"e":18,"c":"pl-k"},{"s":19,"e":22,"c":"pl-c1"},{"s":24,"e":27,"c":"pl-s1"},{"s":28,"e":29,"c":"pl-c1"},{"s":30,"e":36,"c":"pl-s1"},{"s":37,"e":38,"c":"pl-c1"},{"s":40,"e":42,"c":"pl-c1"},{"s":43,"e":48,"c":"pl-s1"},{"s":49,"e":50,"c":"pl-c1"},{"s":51,"e":57,"c":"pl-s1"},{"s":58,"e":59,"c":"pl-c1"},{"s":64,"e":83,"c":"pl-c"}],[{"s":20,"e":25,"c":"pl-s1"},{"s":26,"e":28,"c":"pl-c1"},{"s":29,"e":31,"c":"pl-c1"}],[],[{"s":12,"e":49,"c":"pl-c"}],[{"s":12,"e":15,"c":"pl-k"},{"s":16,"e":21,"c":"pl-s1"},{"s":22,"e":24,"c":"pl-c1"},{"s":25,"e":32,"c":"pl-s1"},{"s":33,"e":40,"c":"pl-s"}],[{"s":16,"e":18,"c":"pl-k"},{"s":19,"e":24,"c":"pl-s1"},{"s":25,"e":28,"c":"pl-c1"},{"s":29,"e":31,"c":"pl-c1"},{"s":32,"e":43,"c":"pl-s1"},{"s":44,"e":51,"c":"pl-s1"},{"s":52,"e":61,"c":"pl-s"},{"s":63,"e":64,"c":"pl-c1"},{"s":65,"e":66,"c":"pl-c1"}],[{"s":20,"e":25,"c":"pl-s1"},{"s":26,"e":28,"c":"pl-c1"},{"s":29,"e":30,"c":"pl-c1"},{"s":33,"e":50,"c":"pl-c"}],[],[{"s":12,"e":41,"c":"pl-c"}],[{"s":12,"e":25,"c":"pl-s1"},{"s":26,"e":30,"c":"pl-s1"},{"s":32,"e":38,"c":"pl-en"},{"s":40,"e":45,"c":"pl-s1"},{"s":47,"e":50,"c":"pl-s1"}],[{"s":12,"e":17,"c":"pl-s1"},{"s":18,"e":20,"c":"pl-c1"},{"s":21,"e":22,"c":"pl-c1"},{"s":24,"e":86,"c":"pl-c"}],[],[{"s":8,"e":14,"c":"pl-k"},{"s":15,"e":20,"c":"pl-s1"}],[],[{"s":4,"e":66,"c":"pl-c"}],[{"s":4,"e":7,"c":"pl-k"},{"s":8,"e":14,"c":"pl-en"},{"s":15,"e":25,"c":"pl-s1"}],[],[{"s":8,"e":60,"c":"pl-c"}],[{"s":8,"e":18,"c":"pl-s1"},{"s":19,"e":23,"c":"pl-en"},{"s":24,"e":27,"c":"pl-s1"},{"s":27,"e":28,"c":"pl-c1"},{"s":28,"e":34,"c":"pl-k"},{"s":35,"e":36,"c":"pl-s1"},{"s":38,"e":45,"c":"pl-en"},{"s":46,"e":47,"c":"pl-s1"},{"s":50,"e":57,"c":"pl-s1"},{"s":57,"e":58,"c":"pl-c1"},{"s":58,"e":62,"c":"pl-c1"}],[],[{"s":8,"e":73,"c":"pl-c"}],[{"s":8,"e":22,"c":"pl-s1"},{"s":23,"e":24,"c":"pl-c1"},{"s":25,"e":35,"c":"pl-s1"},{"s":37,"e":39,"c":"pl-c1"}],[],[{"s":8,"e":90,"c":"pl-c"}],[{"s":8,"e":13,"c":"pl-k"},{"s":14,"e":17,"c":"pl-en"},{"s":18,"e":32,"c":"pl-s1"},{"s":34,"e":35,"c":"pl-c1"},{"s":36,"e":38,"c":"pl-c1"}],[{"s":12,"e":67,"c":"pl-c"}],[{"s":12,"e":14,"c":"pl-s1"},{"s":16,"e":18,"c":"pl-s1"},{"s":19,"e":20,"c":"pl-c1"},{"s":21,"e":27,"c":"pl-s1"},{"s":28,"e":34,"c":"pl-en"},{"s":35,"e":45,"c":"pl-s1"},{"s":47,"e":49,"c":"pl-c1"},{"s":52,"e":53,"c":"pl-c1"}],[],[{"s":12,"e":66,"c":"pl-c"}],[{"s":12,"e":27,"c":"pl-s1"},{"s":28,"e":29,"c":"pl-c1"},{"s":30,"e":36,"c":"pl-s1"},{"s":37,"e":44,"c":"pl-en"},{"s":45,"e":46,"c":"pl-c1"},{"s":48,"e":61,"c":"pl-s1"},{"s":62,"e":63,"c":"pl-c1"},{"s":64,"e":65,"c":"pl-c1"}],[{"s":12,"e":17,"c":"pl-s1"},{"s":18,"e":19,"c":"pl-c1"},{"s":20,"e":22,"c":"pl-s1"},{"s":24,"e":39,"c":"pl-s1"},{"s":41,"e":42,"c":"pl-c1"},{"s":43,"e":45,"c":"pl-s1"},{"s":46,"e":61,"c":"pl-s1"}],[],[{"s":12,"e":81,"c":"pl-c"}],[{"s":12,"e":14,"c":"pl-k"},{"s":15,"e":21,"c":"pl-s1"},{"s":22,"e":28,"c":"pl-en"},{"s":31,"e":32,"c":"pl-c1"},{"s":33,"e":37,"c":"pl-c1"},{"s":40,"e":64,"c":"pl-c"}],[{"s":16,"e":19,"c":"pl-s1"},{"s":20,"e":21,"c":"pl-c1"},{"s":22,"e":28,"c":"pl-s1"},{"s":29,"e":36,"c":"pl-en"},{"s":37,"e":38,"c":"pl-c1"},{"s":40,"e":53,"c":"pl-s1"},{"s":54,"e":55,"c":"pl-c1"},{"s":56,"e":57,"c":"pl-c1"},{"s":60,"e":96,"c":"pl-c"}],[{"s":16,"e":21,"c":"pl-s1"},{"s":22,"e":25,"c":"pl-s1"},{"s":27,"e":33,"c":"pl-s"},{"s":35,"e":36,"c":"pl-c1"},{"s":37,"e":43,"c":"pl-s1"},{"s":44,"e":51,"c":"pl-en"},{"s":52,"e":53,"c":"pl-c1"},{"s":55,"e":64,"c":"pl-s1"},{"s":67,"e":94,"c":"pl-c"}],[{"s":16,"e":21,"c":"pl-s1"},{"s":22,"e":25,"c":"pl-s1"},{"s":27,"e":39,"c":"pl-s"},{"s":41,"e":42,"c":"pl-c1"},{"s":43,"e":49,"c":"pl-s1"},{"s":50,"e":57,"c":"pl-en"},{"s":58,"e":59,"c":"pl-c1"},{"s":61,"e":75,"c":"pl-s1"},{"s":76,"e":77,"c":"pl-c1"},{"s":78,"e":92,"c":"pl-s1"},{"s":93,"e":96,"c":"pl-s1"},{"s":98,"e":99,"c":"pl-c1"},{"s":100,"e":101,"c":"pl-c1"},{"s":104,"e":137,"c":"pl-c"}],[],[{"s":12,"e":58,"c":"pl-c"}],[{"s":12,"e":26,"c":"pl-s1"},{"s":27,"e":33,"c":"pl-en"},{"s":34,"e":39,"c":"pl-s1"}],[],[{"s":8,"e":14,"c":"pl-k"},{"s":15,"e":29,"c":"pl-s1"}],[],[{"s":4,"e":74,"c":"pl-c"}],[{"s":4,"e":7,"c":"pl-k"},{"s":8,"e":9,"c":"pl-s1"},{"s":10,"e":12,"c":"pl-c1"},{"s":13,"e":18,"c":"pl-en"},{"s":19,"e":21,"c":"pl-c1"},{"s":25,"e":50,"c":"pl-c"}],[{"s":8,"e":18,"c":"pl-s1"},{"s":19,"e":20,"c":"pl-c1"},{"s":21,"e":27,"c":"pl-en"},{"s":28,"e":38,"c":"pl-s1"},{"s":41,"e":65,"c":"pl-c"}],[],[{"s":4,"e":65,"c":"pl-c"}],[{"s":4,"e":17,"c":"pl-s1"},{"s":18,"e":19,"c":"pl-c1"},{"s":20,"e":23,"c":"pl-en"},{"s":24,"e":34,"c":"pl-s1"},{"s":36,"e":39,"c":"pl-s1"},{"s":39,"e":40,"c":"pl-c1"},{"s":40,"e":46,"c":"pl-k"},{"s":47,"e":48,"c":"pl-s1"},{"s":50,"e":57,"c":"pl-en"},{"s":58,"e":59,"c":"pl-s1"}],[],[{"s":4,"e":43,"c":"pl-c"}],[{"s":4,"e":18,"c":"pl-s1"},{"s":19,"e":20,"c":"pl-c1"}],[{"s":4,"e":7,"c":"pl-k"},{"s":8,"e":15,"c":"pl-s1"},{"s":16,"e":18,"c":"pl-c1"},{"s":19,"e":32,"c":"pl-s1"}],[{"s":8,"e":22,"c":"pl-s1"},{"s":23,"e":29,"c":"pl-en"}],[{"s":12,"e":21,"c":"pl-s"},{"s":23,"e":30,"c":"pl-s1"},{"s":31,"e":40,"c":"pl-s"}],[{"s":12,"e":18,"c":"pl-s"},{"s":20,"e":27,"c":"pl-s1"},{"s":28,"e":34,"c":"pl-s"}],[{"s":12,"e":19,"c":"pl-s"},{"s":21,"e":71,"c":"pl-s"},{"s":23,"e":46,"c":"pl-s1"},{"s":23,"e":24,"c":"pl-kos"},{"s":24,"e":31,"c":"pl-s1"},{"s":32,"e":44,"c":"pl-s"},{"s":45,"e":46,"c":"pl-kos"},{"s":49,"e":70,"c":"pl-s1"},{"s":49,"e":50,"c":"pl-kos"},{"s":50,"e":57,"c":"pl-s1"},{"s":58,"e":68,"c":"pl-s"},{"s":69,"e":70,"c":"pl-kos"}],[{"s":12,"e":19,"c":"pl-s"},{"s":21,"e":25,"c":"pl-s"},{"s":26,"e":30,"c":"pl-en"},{"s":31,"e":34,"c":"pl-en"},{"s":35,"e":38,"c":"pl-s1"},{"s":40,"e":47,"c":"pl-s1"},{"s":48,"e":55,"c":"pl-s"},{"s":59,"e":61,"c":"pl-k"},{"s":62,"e":69,"c":"pl-s1"},{"s":70,"e":77,"c":"pl-s"},{"s":79,"e":83,"c":"pl-k"},{"s":84,"e":103,"c":"pl-s"}],[],[],[{"s":4,"e":10,"c":"pl-k"},{"s":11,"e":25,"c":"pl-s1"}],[],[{"s":0,"e":20,"c":"pl-c"}],[{"s":0,"e":2,"c":"pl-k"},{"s":3,"e":11,"c":"pl-s1"},{"s":12,"e":14,"c":"pl-c1"},{"s":15,"e":25,"c":"pl-s"}],[{"s":4,"e":7,"c":"pl-s1"},{"s":8,"e":11,"c":"pl-en"},{"s":12,"e":17,"c":"pl-s1"},{"s":17,"e":18,"c":"pl-c1"},{"s":18,"e":22,"c":"pl-c1"}],[],[],[],[],[]],"colorizedLines":null,"csv":null,"csvError":null,"dependabotInfo":{"showConfigurationBanner":false,"configFilePath":null,"networkDependabotPath":"/SumaikaImran/AI_LABS/network/updates","dismissConfigurationNoticePath":"/settings/dismiss-notice/dependabot_configuration_notice","configurationNoticeDismissed":false},"displayName":"app.py","displayUrl":"https://github.com/SumaikaImran/AI_LABS/blob/main/app.py?raw=true","headerInfo":{"blobSize":"9.07 KB","deleteTooltip":"Fork this repository and delete the file","editTooltip":"Fork this repository and edit the file","ghDesktopPath":"https://desktop.github.com","isGitLfs":false,"onBranch":true,"shortPath":"730fe53","siteNavLoginPath":"/login?return_to=https%3A%2F%2Fgithub.com%2FSumaikaImran%2FAI_LABS%2Fblob%2Fmain%2Fapp.py","isCSV":false,"isRichtext":false,"toc":null,"lineInfo":{"truncatedLoc":"207","truncatedSloc":"164"},"mode":"file"},"image":false,"isCodeownersFile":null,"isPlain":false,"isValidLegacyIssueTemplate":false,"issueTemplate":null,"discussionTemplate":null,"language":"Python","languageID":303,"large":false,"planSupportInfo":{"repoIsFork":null,"repoOwnedByCurrentUser":null,"requestFullPath":"/SumaikaImran/AI_LABS/blob/main/app.py","showFreeOrgGatedFeatureMessage":null,"showPlanSupportBanner":null,"upgradeDataAttributes":null,"upgradePath":null},"publishBannersInfo":{"dismissActionNoticePath":"/settings/dismiss-notice/publish_action_from_dockerfile","releasePath":"/SumaikaImran/AI_LABS/releases/new?marketplace=true","showPublishActionBanner":false},"rawBlobUrl":"https://github.com/SumaikaImran/AI_LABS/raw/refs/heads/main/app.py","renderImageOrRaw":false,"richText":null,"renderedFileInfo":null,"shortPath":null,"symbolsEnabled":true,"tabSize":8,"topBannersInfo":{"overridingGlobalFundingFile":false,"globalPreferredFundingPath":null,"showInvalidCitationWarning":false,"citationHelpUrl":"https://docs.github.com/github/creating-cloning-and-archiving-repositories/creating-a-repository-on-github/about-citation-files","actionsOnboardingTip":null},"truncated":false,"viewable":true,"workflowRedirectUrl":null,"symbols":{"timed_out":false,"not_analyzed":false,"symbols":[{"name":"app","kind":"constant","ident_start":55,"ident_end":58,"extent_start":55,"extent_end":76,"fully_qualified_name":"app","ident_utf16":{"start":{"line_number":3,"utf16_col":0},"end":{"line_number":3,"utf16_col":3}},"extent_utf16":{"start":{"line_number":3,"utf16_col":0},"end":{"line_number":3,"utf16_col":21}}},{"name":"index","kind":"function","ident_start":128,"ident_end":133,"extent_start":124,"extent_end":178,"fully_qualified_name":"index","ident_utf16":{"start":{"line_number":7,"utf16_col":4},"end":{"line_number":7,"utf16_col":9}},"extent_utf16":{"start":{"line_number":7,"utf16_col":0},"end":{"line_number":8,"utf16_col":40}}},{"name":"generate_schedule","kind":"function","ident_start":293,"ident_end":310,"extent_start":289,"extent_end":2502,"fully_qualified_name":"generate_schedule","ident_utf16":{"start":{"line_number":12,"utf16_col":4},"end":{"line_number":12,"utf16_col":21}},"extent_utf16":{"start":{"line_number":12,"utf16_col":0},"end":{"line_number":54,"utf16_col":77}}},{"name":"genetic_algorithm","kind":"function","ident_start":2574,"ident_end":2591,"extent_start":2570,"extent_end":9196,"fully_qualified_name":"genetic_algorithm","ident_utf16":{"start":{"line_number":57,"utf16_col":4},"end":{"line_number":57,"utf16_col":21}},"extent_utf16":{"start":{"line_number":57,"utf16_col":0},"end":{"line_number":197,"utf16_col":25}}},{"name":"fitness","kind":"function","ident_start":5733,"ident_end":5740,"extent_start":5729,"extent_end":7003,"fully_qualified_name":"fitness","ident_utf16":{"start":{"line_number":116,"utf16_col":8},"end":{"line_number":116,"utf16_col":15}},"extent_utf16":{"start":{"line_number":116,"utf16_col":4},"end":{"line_number":149,"utf16_col":20}}},{"name":"evolve","kind":"function","ident_start":7082,"ident_end":7088,"extent_start":7078,"extent_end":8430,"fully_qualified_name":"evolve","ident_utf16":{"start":{"line_number":152,"utf16_col":8},"end":{"line_number":152,"utf16_col":14}},"extent_utf16":{"start":{"line_number":152,"utf16_col":4},"end":{"line_number":178,"utf16_col":29}}}]}},"copilotInfo":{"documentationUrl":"https://docs.github.com/copilot/overview-of-github-copilot/about-github-copilot-for-individuals","notices":{"codeViewPopover":{"dismissed":false,"dismissPath":"/settings/dismiss-notice/code_view_copilot_popover"}},"userAccess":{"hasSubscriptionEnded":false,"orgHasCFBAccess":false,"userHasCFIAccess":false,"userHasOrgs":false,"userIsOrgAdmin":false,"userIsOrgMember":false,"business":null,"featureRequestInfo":null}},"copilotAccessAllowed":false,"csrf_tokens":{"/SumaikaImran/AI_LABS/branches":{"post":"AB8i9HTYHnqg892KfNBa3p_7vH6IsU2gNXQqeKrsH_kM6IHwtHPwKPa_QfojB4XuVsUv333nzK-Y8ddWsWnZxw"},"/repos/preferences":{"post":"TJtLHhGYAR3JY6ZtUF_E0iiRr-bHy8ZI_uEYvwgsMm7yF9hRt8-SyJlnRX5fN6yqkpjIxu-hU1gByQhA1K5GlQ"}}},"title":"AI_LABS/app.py at main · SumaikaImran/AI_LABS","appPayload":{"helpUrl":"https://docs.github.com","findFileWorkerPath":"/assets-cdn/worker/find-file-worker-1583894afd38.js","findInFileWorkerPath":"/assets-cdn/worker/find-in-file-worker-67668e8c2caa.js","githubDevUrl":"https://github.dev/","enabled_features":{"code_nav_ui_events":false,"overview_shared_code_dropdown_button":false,"react_blob_overlay":false,"copilot_conversational_ux_embedding_update":false,"copilot_smell_icebreaker_ux":true,"copilot_workspace":false,"accessible_code_button":true}}}</script>
  <div data-target="react-app.reactRoot"><meta data-hydrostats="publish"> <!-- --> <!-- --> <button hidden="" data-testid="header-permalink-button" data-hotkey-scope="read-only-cursor-text-area" data-hotkey="y,Shift+Y"></button><button hidden="" data-hotkey="y,Shift+Y"></button><div><div style="--sticky-pane-height: calc(100vh - (max(104px, 0px)));" class="Box-sc-g0xbh4-0 hOfjFo"><div class="Box-sc-g0xbh4-0 oDGAe"><div class="Box-sc-g0xbh4-0 kowOcT"><div tabindex="0" class="Box-sc-g0xbh4-0 gISSDQ"><div class="Box-sc-g0xbh4-0 MZXzw"><div class="Box-sc-g0xbh4-0 hPvFuC"></div><div style="--pane-width:320px" class="Box-sc-g0xbh4-0 fFSoPl"><div><div id="repos-file-tree" class="Box-sc-g0xbh4-0 bNhwaa"><div class="Box-sc-g0xbh4-0 hNNCwk"><div class="Box-sc-g0xbh4-0 jfIeyl"><h2 class="Box-sc-g0xbh4-0 XosP prc-Heading-Heading-6CmGO"><span role="tooltip" aria-label="Collapse file tree" id="expand-button-file-tree-button" class="Tooltip__TooltipBase-sc-17tf59c-0 hWlpPn tooltipped-se"><button data-component="IconButton" type="button" data-testid="collapse-file-tree-button" aria-expanded="true" aria-controls="repos-file-tree" class="prc-Button-ButtonBase-c50BI position-relative ExpandFileTreeButton-module__expandButton--gL4is fgColor-muted prc-Button-IconButton-szpyj" data-loading="false" data-no-visuals="true" data-size="medium" data-variant="invisible" aria-describedby=":R356mplab:-loading-announcement" aria-labelledby="expand-button-file-tree-button" data-hotkey="Control+b"><svg aria-hidden="true" focusable="false" class="octicon octicon-sidebar-expand" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display:inline-block;user-select:none;vertical-align:text-bottom;overflow:visible"><path d="m4.177 7.823 2.396-2.396A.25.25 0 0 1 7 5.604v4.792a.25.25 0 0 1-.427.177L4.177 8.177a.25.25 0 0 1 0-.354Z"></path><path d="M0 1.75C0 .784.784 0 1.75 0h12.5C15.216 0 16 .784 16 1.75v12.5A1.75 1.75 0 0 1 14.25 16H1.75A1.75 1.75 0 0 1 0 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25H9.5v-13Zm12.5 13a.25.25 0 0 0 .25-.25V1.75a.25.25 0 0 0-.25-.25H11v13Z"></path></svg></button></span><button hidden="" data-testid="" data-hotkey-scope="read-only-cursor-text-area" data-hotkey="Control+b"></button></h2><h2 class="Box-sc-g0xbh4-0 kOkWgo prc-Heading-Heading-6CmGO">Files</h2></div><div class="Box-sc-g0xbh4-0 lhbroM"><div class="Box-sc-g0xbh4-0 khzwtX"><button type="button" aria-haspopup="true" aria-expanded="false" tabindex="0" aria-label="main branch" data-testid="anchor-button" class="Box-sc-g0xbh4-0 gMOVLe prc-Button-ButtonBase-c50BI react-repos-tree-pane-ref-selector width-full ref-selector-class" data-loading="false" data-size="medium" data-variant="default" aria-describedby="branch-picker-repos-header-ref-selector-loading-announcement" id="branch-picker-repos-header-ref-selector" data-hotkey="w"><span data-component="buttonContent" class="Box-sc-g0xbh4-0 gUkoLg prc-Button-ButtonContent-HKbr-"><span data-component="text" class="prc-Button-Label-pTQ3x"><div class="Box-sc-g0xbh4-0 bZBlpz"><div class="Box-sc-g0xbh4-0 lhTYNA"><svg aria-hidden="true" focusable="false" class="octicon octicon-git-branch" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display:inline-block;user-select:none;vertical-align:text-bottom;overflow:visible"><path d="M9.5 3.25a2.25 2.25 0 1 1 3 2.122V6A2.5 2.5 0 0 1 10 8.5H6a1 1 0 0 0-1 1v1.128a2.251 2.251 0 1 1-1.5 0V5.372a2.25 2.25 0 1 1 1.5 0v1.836A2.493 2.493 0 0 1 6 7h4a1 1 0 0 0 1-1v-.628A2.25 2.25 0 0 1 9.5 3.25Zm-6 0a.75.75 0 1 0 1.5 0 .75.75 0 0 0-1.5 0Zm8.25-.75a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5ZM4.25 12a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5Z"></path></svg></div><div class="Box-sc-g0xbh4-0 ffLUq ref-selector-button-text-container"><span class="Box-sc-g0xbh4-0 bmcJak prc-Text-Text-0ima0">&nbsp;<!-- -->main</span></div></div></span><span data-component="trailingVisual" class="prc-Button-Visual-2epfX prc-Button-VisualWrap-Db-eB"><svg aria-hidden="true" focusable="false" class="octicon octicon-triangle-down" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display:inline-block;user-select:none;vertical-align:text-bottom;overflow:visible"><path d="m4.427 7.427 3.396 3.396a.25.25 0 0 0 .354 0l3.396-3.396A.25.25 0 0 0 11.396 7H4.604a.25.25 0 0 0-.177.427Z"></path></svg></span></span></button><button hidden="" data-hotkey-scope="read-only-cursor-text-area" data-hotkey="w"></button></div><div class="Box-sc-g0xbh4-0 eTeVqd"><span role="tooltip" aria-label="Add file" id=":Rq6mplab:" class="Tooltip__TooltipBase-sc-17tf59c-0 hWlpPn tooltipped-s"><a sx="[object Object]" data-component="IconButton" type="button" aria-label="Add file" class="Box-sc-g0xbh4-0 fhbevO prc-Button-ButtonBase-c50BI prc-Button-IconButton-szpyj" data-loading="false" data-no-visuals="true" data-size="medium" data-variant="default" aria-describedby=":R2q6mplab:-loading-announcement" href="https://github.com/SumaikaImran/AI_LABS/new/main"><svg aria-hidden="true" focusable="false" class="octicon octicon-plus" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display:inline-block;user-select:none;vertical-align:text-bottom;overflow:visible"><path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path></svg></a></span><button data-component="IconButton" type="button" aria-label="Search this repository" class="Box-sc-g0xbh4-0 fCjIQM prc-Button-ButtonBase-c50BI prc-Button-IconButton-szpyj" data-loading="false" data-no-visuals="true" data-size="medium" data-variant="default" aria-describedby=":R3a6mplab:-loading-announcement" data-hotkey="/"><svg aria-hidden="true" focusable="false" class="octicon octicon-search" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display:inline-block;user-select:none;vertical-align:text-bottom;overflow:visible"><path d="M10.68 11.74a6 6 0 0 1-7.922-8.982 6 6 0 0 1 8.982 7.922l3.04 3.04a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215ZM11.5 7a4.499 4.499 0 1 0-8.997 0A4.499 4.499 0 0 0 11.5 7Z"></path></svg></button><button hidden="" data-testid="" data-hotkey-scope="read-only-cursor-text-area" data-hotkey="/"></button></div></div></div><div class="Box-sc-g0xbh4-0 qkmJR"><span class="TextInputWrapper__TextInputBaseWrapper-sc-1mqhpbi-0 TextInputWrapper-sc-1mqhpbi-1 gwqFqs decvaq TextInput-wrapper" aria-busy="false"><span class="TextInput-icon" id=":R5amplab:" aria-hidden="true"><svg aria-hidden="true" focusable="false" class="octicon octicon-search" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display:inline-block;user-select:none;vertical-align:text-bottom;overflow:visible"><path d="M10.68 11.74a6 6 0 0 1-7.922-8.982 6 6 0 0 1 8.982 7.922l3.04 3.04a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215ZM11.5 7a4.499 4.499 0 1 0-8.997 0A4.499 4.499 0 0 0 11.5 7Z"></path></svg></span><input type="text" aria-label="Go to file" role="combobox" aria-controls="file-results-list" aria-expanded="false" aria-haspopup="dialog" autocorrect="off" spellcheck="false" placeholder="Go to file" aria-describedby=":R5amplab: :R5amplabH1:" data-component="input" class="UnstyledTextInput-sc-14ypya-0 kbCLEG" value=""><span class="TextInput-icon" id=":R5amplabH1:" aria-hidden="true"><div class="Box-sc-g0xbh4-0 dItACB"><kbd>t</kbd></div></span></span></div><button hidden="" data-testid="" data-hotkey-scope="read-only-cursor-text-area" data-hotkey="t,Shift+T"></button><button hidden="" data-hotkey="t,Shift+T"></button><div class="Box-sc-g0xbh4-0 jbQqON"><div><div class="react-tree-show-tree-items"><div data-testid="repos-file-tree-container" class="Box-sc-g0xbh4-0 cOxzdh"><nav aria-label="File Tree Navigation"><span role="status" aria-live="polite" aria-atomic="true" class="_VisuallyHidden__VisuallyHidden-sc-11jhm7a-0 brGdpi"></span><ul role="tree" aria-label="Files" data-truncate-text="true" class="TreeView__UlBox-sc-4ex6b6-0 gnOBko"><li class="PRIVATE_TreeView-item" tabindex="-1" id="IDS.py-item" role="treeitem" aria-labelledby=":rr:" aria-describedby=":rs:" aria-level="1" aria-selected="false"><div class="PRIVATE_TreeView-item-container" style="--level: 1; content-visibility: auto; contain-intrinsic-size: auto 2rem;"><div style="grid-area: spacer; display: flex;"><div style="width: 100%; display: flex;"></div></div><div id=":rr:" class="PRIVATE_TreeView-item-content"><div class="PRIVATE_VisuallyHidden" aria-hidden="true" id=":rs:"></div><div class="PRIVATE_TreeView-item-visual" aria-hidden="true"><svg aria-hidden="true" focusable="false" class="octicon octicon-file" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display: inline-block; user-select: none; vertical-align: text-bottom; overflow: visible;"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg></div><span class="PRIVATE_TreeView-item-content-text"><span>IDS.py</span></span></div></div></li><li class="PRIVATE_TreeView-item" tabindex="-1" id="ai lab8_9.pdf-item" role="treeitem" aria-labelledby=":ru:" aria-describedby=":rv:" aria-level="1" aria-selected="false"><div class="PRIVATE_TreeView-item-container" style="--level: 1; content-visibility: auto; contain-intrinsic-size: auto 2rem;"><div style="grid-area: spacer; display: flex;"><div style="width: 100%; display: flex;"></div></div><div id=":ru:" class="PRIVATE_TreeView-item-content"><div class="PRIVATE_VisuallyHidden" aria-hidden="true" id=":rv:"></div><div class="PRIVATE_TreeView-item-visual" aria-hidden="true"><svg aria-hidden="true" focusable="false" class="octicon octicon-file" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display: inline-block; user-select: none; vertical-align: text-bottom; overflow: visible;"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg></div><span class="PRIVATE_TreeView-item-content-text"><span>ai lab8_9.pdf</span></span></div></div></li><li class="PRIVATE_TreeView-item" tabindex="0" id="app.py-item" role="treeitem" aria-labelledby=":r11:" aria-describedby=":r12:" aria-level="1" aria-current="true" aria-selected="false"><div class="PRIVATE_TreeView-item-container" style="--level: 1;"><div style="grid-area: spacer; display: flex;"><div style="width: 100%; display: flex;"></div></div><div id=":r11:" class="PRIVATE_TreeView-item-content"><div class="PRIVATE_VisuallyHidden" aria-hidden="true" id=":r12:"></div><div class="PRIVATE_TreeView-item-visual" aria-hidden="true"><svg aria-hidden="true" focusable="false" class="octicon octicon-file" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display: inline-block; user-select: none; vertical-align: text-bottom; overflow: visible;"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg></div><span class="PRIVATE_TreeView-item-content-text"><span>app.py</span></span></div></div></li></ul></nav></div></div></div></div></div></div></div><div class="Box-sc-g0xbh4-0 tLGNc"><div role="slider" aria-label="Draggable pane splitter" aria-valuemin="256" aria-valuemax="407" aria-valuenow="320" aria-valuetext="Pane width 320 pixels" tabindex="0" class="Box-sc-g0xbh4-0 bHLmSv"></div></div></div></div><div class="Box-sc-g0xbh4-0 iKqMNA"><div class="Box-sc-g0xbh4-0"></div><div class="Box-sc-g0xbh4-0 FxAyp"><div data-selector="repos-split-pane-content" tabindex="0" class="Box-sc-g0xbh4-0 leYMvG"><div class="Box-sc-g0xbh4-0 KMPzq"><div class="Box-sc-g0xbh4-0 hfKjHv container"><div class="px-3 pt-3 pb-0" id="StickyHeader"><div class="Box-sc-g0xbh4-0 gZWyZE"><div class="Box-sc-g0xbh4-0 dwYKDk"><div class="Box-sc-g0xbh4-0 iDtIiT"><div class="Box-sc-g0xbh4-0 cEytCf"><nav data-testid="breadcrumbs" aria-labelledby="repos-header-breadcrumb--wide-heading" id="repos-header-breadcrumb--wide" class="Box-sc-g0xbh4-0 fzFXnm"><h2 class="sr-only prc-Heading-Heading-6CmGO" data-testid="screen-reader-heading" id="repos-header-breadcrumb--wide-heading">Breadcrumbs</h2><ol class="Box-sc-g0xbh4-0 iMnkmv"><li class="Box-sc-g0xbh4-0 ghzDag"><a class="Box-sc-g0xbh4-0 kHuKdh prc-Link-Link-85e08" sx="[object Object]" data-testid="breadcrumbs-repo-link" href="https://github.com/SumaikaImran/AI_LABS/tree/main">AI_LABS</a></li></ol></nav><div data-testid="breadcrumbs-filename" class="Box-sc-g0xbh4-0 ghzDag"><span class="Box-sc-g0xbh4-0 hzJBof prc-Text-Text-0ima0" aria-hidden="true">/</span><h1 class="Box-sc-g0xbh4-0 jGhzSQ prc-Heading-Heading-6CmGO" tabindex="-1" id="file-name-id-wide">app.py</h1></div><div aria-describedby=":Rdd9lab:"><button data-component="IconButton" type="button" aria-label="Copy path" tabindex="0" class="Box-sc-g0xbh4-0 prc-Button-ButtonBase-c50BI prc-Button-IconButton-szpyj" data-loading="false" data-no-visuals="true" data-size="small" data-variant="invisible" aria-describedby=":R1td9lab:-loading-announcement"><svg aria-hidden="true" focusable="false" class="octicon octicon-copy" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display:inline-block;user-select:none;vertical-align:text-bottom;overflow:visible"><path d="M0 6.75C0 5.784.784 5 1.75 5h1.5a.75.75 0 0 1 0 1.5h-1.5a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-1.5a.75.75 0 0 1 1.5 0v1.5A1.75 1.75 0 0 1 9.25 16h-7.5A1.75 1.75 0 0 1 0 14.25Z"></path><path d="M5 1.75C5 .784 5.784 0 6.75 0h7.5C15.216 0 16 .784 16 1.75v7.5A1.75 1.75 0 0 1 14.25 11h-7.5A1.75 1.75 0 0 1 5 9.25Zm1.75-.25a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-7.5a.25.25 0 0 0-.25-.25Z"></path></svg></button></div></div></div><div class="react-code-view-header-element--wide"><div class="Box-sc-g0xbh4-0 faNtbn"><div class="d-flex gap-2"> <button hidden="" data-testid="" data-hotkey-scope="read-only-cursor-text-area" data-hotkey="l,Shift+L"></button><button hidden="" data-hotkey="l,Shift+L"></button><button hidden="" data-testid="" data-hotkey-scope="read-only-cursor-text-area" data-hotkey="Mod+Alt+g"></button><button hidden="" data-hotkey="Mod+Alt+g"></button><button type="button" class="Box-sc-g0xbh4-0 dwNhzn prc-Button-ButtonBase-c50BI" data-loading="false" data-no-visuals="true" data-size="medium" data-variant="default" aria-describedby=":R2l6d9lab:-loading-announcement" data-hotkey="b,Shift+B,Control+/ Control+b"><span data-component="buttonContent" class="Box-sc-g0xbh4-0 gUkoLg prc-Button-ButtonContent-HKbr-"><span data-component="text" class="prc-Button-Label-pTQ3x">Blame</span></span></button><button hidden="" data-testid="" data-hotkey-scope="read-only-cursor-text-area" data-hotkey="b,Shift+B,Control+/ Control+b"></button><button data-component="IconButton" type="button" aria-label="More file actions" title="More file actions" data-testid="more-file-actions-button-nav-menu-wide" aria-haspopup="true" aria-expanded="false" tabindex="0" class="Box-sc-g0xbh4-0 fGwBZA prc-Button-ButtonBase-c50BI js-blob-dropdown-click prc-Button-IconButton-szpyj" data-loading="false" data-no-visuals="true" data-size="medium" data-variant="default" aria-describedby=":R156d9lab:-loading-announcement" id=":R156d9lab:"><svg aria-hidden="true" focusable="false" class="octicon octicon-kebab-horizontal" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display:inline-block;user-select:none;vertical-align:text-bottom;overflow:visible"><path d="M8 9a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3ZM1.5 9a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Zm13 0a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Z"></path></svg></button> </div></div></div><div class="react-code-view-header-element--narrow"><div class="Box-sc-g0xbh4-0 faNtbn"><div class="d-flex gap-2"> <button hidden="" data-testid="" data-hotkey-scope="read-only-cursor-text-area" data-hotkey="l,Shift+L"></button><button hidden="" data-hotkey="l,Shift+L"></button><button hidden="" data-testid="" data-hotkey-scope="read-only-cursor-text-area" data-hotkey="Mod+Alt+g"></button><button hidden="" data-hotkey="Mod+Alt+g"></button><button type="button" class="Box-sc-g0xbh4-0 dwNhzn prc-Button-ButtonBase-c50BI" data-loading="false" data-no-visuals="true" data-size="medium" data-variant="default" aria-describedby=":R2l7d9lab:-loading-announcement" data-hotkey="b,Shift+B,Control+/ Control+b"><span data-component="buttonContent" class="Box-sc-g0xbh4-0 gUkoLg prc-Button-ButtonContent-HKbr-"><span data-component="text" class="prc-Button-Label-pTQ3x">Blame</span></span></button><button hidden="" data-testid="" data-hotkey-scope="read-only-cursor-text-area" data-hotkey="b,Shift+B,Control+/ Control+b"></button><button data-component="IconButton" type="button" aria-label="More file actions" title="More file actions" data-testid="more-file-actions-button-nav-menu-narrow" aria-haspopup="true" aria-expanded="false" tabindex="0" class="Box-sc-g0xbh4-0 fGwBZA prc-Button-ButtonBase-c50BI js-blob-dropdown-click prc-Button-IconButton-szpyj" data-loading="false" data-no-visuals="true" data-size="medium" data-variant="default" aria-describedby=":R157d9lab:-loading-announcement" id=":R157d9lab:"><svg aria-hidden="true" focusable="false" class="octicon octicon-kebab-horizontal" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display:inline-block;user-select:none;vertical-align:text-bottom;overflow:visible"><path d="M8 9a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3ZM1.5 9a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Zm13 0a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Z"></path></svg></button> </div></div></div></div></div></div></div></div><div class="Box-sc-g0xbh4-0 dJxjrT react-code-view-bottom-padding"> <div class="Box-sc-g0xbh4-0 eFxKDQ"></div> <!-- --> <!-- --> </div><div class="Box-sc-g0xbh4-0 dJxjrT"> <!-- --> <!-- --> <button hidden="" data-testid="" data-hotkey-scope="read-only-cursor-text-area" data-hotkey="r,Shift+R"></button><button hidden="" data-hotkey="r,Shift+R"></button><div class="d-flex flex-column border rounded-2 mb-3 pl-1"><div class="Box-sc-g0xbh4-0 dzCJzi"><h2 class="sr-only prc-Heading-Heading-6CmGO" data-testid="screen-reader-heading">Latest commit</h2><div data-testid="latest-commit" class="Box-sc-g0xbh4-0 ePWWCk"><div class="Box-sc-g0xbh4-0 dpBUfI"><div data-testid="author-avatar" class="Box-sc-g0xbh4-0 hKWjvQ"><a class="prc-Link-Link-85e08" href="https://github.com/SumaikaImran" data-testid="avatar-icon-link" data-hovercard-url="/users/SumaikaImran/hovercard"><img data-component="Avatar" class="Box-sc-g0xbh4-0 cvdqJW prc-Avatar-Avatar-ZRS-m" alt="SumaikaImran" width="20" height="20" src="./app_files/147117851" data-testid="github-avatar" aria-label="SumaikaImran" style="--avatarSize-regular: 20px;"></a><a class="Box-sc-g0xbh4-0 dkaFxu prc-Link-Link-85e08" data-muted="true" href="https://github.com/SumaikaImran/AI_LABS/commits?author=SumaikaImran" aria-label="commits by SumaikaImran" data-hovercard-url="/users/SumaikaImran/hovercard">SumaikaImran</a></div><span class=""></span></div><div class="Box-sc-g0xbh4-0 erEOeb d-none d-sm-flex"><div class="Truncate flex-items-center f5"><span class="Truncate-text prc-Text-Text-0ima0" data-testid="latest-commit-html"><a href="https://github.com/SumaikaImran/AI_LABS/commit/ecc18724171763305792a131a1a971cbb6ed8b40" class="Link--secondary" data-pjax="true" data-hovercard-url="/SumaikaImran/AI_LABS/commit/ecc18724171763305792a131a1a971cbb6ed8b40/hovercard">Add files via upload</a></span></div></div><span class="d-flex d-sm-none fgColor-muted f6"><relative-time class="sc-aXZVg" tense="past" datetime="2024-11-26T17:11:08.000Z" title="Nov 26, 2024, 10:11 PM GMT+5"><template shadowrootmode="open">2 days ago</template>Nov 26, 2024</relative-time></span></div><div class="d-flex flex-shrink-0 gap-2"><div data-testid="latest-commit-details" class="d-none d-sm-flex flex-items-center"><span class="d-flex flex-nowrap fgColor-muted f6"><a class="Link--secondary prc-Link-Link-85e08" aria-label="Commit ecc1872" data-hovercard-url="/SumaikaImran/AI_LABS/commit/ecc18724171763305792a131a1a971cbb6ed8b40/hovercard" href="https://github.com/SumaikaImran/AI_LABS/commit/ecc18724171763305792a131a1a971cbb6ed8b40">ecc1872</a>&nbsp;·&nbsp;<relative-time class="sc-aXZVg" tense="past" datetime="2024-11-26T17:11:08.000Z" title="Nov 26, 2024, 10:11 PM GMT+5"><template shadowrootmode="open">2 days ago</template>Nov 26, 2024</relative-time></span></div><div class="d-flex gap-2"><h2 class="sr-only prc-Heading-Heading-6CmGO" data-testid="screen-reader-heading">History</h2><a href="https://github.com/SumaikaImran/AI_LABS/commits/main/app.py" class="prc-Button-ButtonBase-c50BI d-none d-lg-flex LinkButton-module__code-view-link-button--xvCGA flex-items-center fgColor-default" data-loading="false" data-size="small" data-variant="invisible" aria-describedby=":R5dlal9lab:-loading-announcement"><span data-component="buttonContent" data-align="center" class="prc-Button-ButtonContent-HKbr-"><span data-component="leadingVisual" class="prc-Button-Visual-2epfX prc-Button-VisualWrap-Db-eB"><svg aria-hidden="true" focusable="false" class="octicon octicon-history" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display:inline-block;user-select:none;vertical-align:text-bottom;overflow:visible"><path d="m.427 1.927 1.215 1.215a8.002 8.002 0 1 1-1.6 5.685.75.75 0 1 1 1.493-.154 6.5 6.5 0 1 0 1.18-4.458l1.358 1.358A.25.25 0 0 1 3.896 6H.25A.25.25 0 0 1 0 5.75V2.104a.25.25 0 0 1 .427-.177ZM7.75 4a.75.75 0 0 1 .75.75v2.992l2.028.812a.75.75 0 0 1-.557 1.392l-2.5-1A.751.751 0 0 1 7 8.25v-3.5A.75.75 0 0 1 7.75 4Z"></path></svg></span><span data-component="text" class="prc-Button-Label-pTQ3x"><span class="fgColor-default">History</span></span></span></a><div class="d-sm-none"><button data-component="IconButton" type="button" aria-label="Open commit details" aria-pressed="false" aria-expanded="false" data-testid="latest-commit-details-toggle" class="Box-sc-g0xbh4-0 hdOVEE prc-Button-ButtonBase-c50BI prc-Button-IconButton-szpyj" data-loading="false" data-no-visuals="true" data-size="small" data-variant="invisible" aria-describedby=":r18:-loading-announcement"><svg aria-hidden="true" focusable="false" class="octicon octicon-ellipsis" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display: inline-block; user-select: none; vertical-align: text-bottom; overflow: visible;"><path d="M0 5.75C0 4.784.784 4 1.75 4h12.5c.966 0 1.75.784 1.75 1.75v4.5A1.75 1.75 0 0 1 14.25 12H1.75A1.75 1.75 0 0 1 0 10.25ZM12 7a1 1 0 1 0 0 2 1 1 0 0 0 0-2ZM7 8a1 1 0 1 0 2 0 1 1 0 0 0-2 0ZM4 7a1 1 0 1 0 0 2 1 1 0 0 0 0-2Z"></path></svg></button></div><div class="d-flex d-lg-none"><span role="tooltip" aria-label="History" id="history-icon-button-tooltip" class="Tooltip__TooltipBase-sc-17tf59c-0 hWlpPn tooltipped-n"><a href="https://github.com/SumaikaImran/AI_LABS/commits/main/app.py" class="prc-Button-ButtonBase-c50BI LinkButton-module__code-view-link-button--xvCGA flex-items-center fgColor-default" data-loading="false" data-size="small" data-variant="invisible" aria-describedby=":Rpdlal9lab:-loading-announcement history-icon-button-tooltip"><span data-component="buttonContent" data-align="center" class="prc-Button-ButtonContent-HKbr-"><span data-component="leadingVisual" class="prc-Button-Visual-2epfX prc-Button-VisualWrap-Db-eB"><svg aria-hidden="true" focusable="false" class="octicon octicon-history" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display:inline-block;user-select:none;vertical-align:text-bottom;overflow:visible"><path d="m.427 1.927 1.215 1.215a8.002 8.002 0 1 1-1.6 5.685.75.75 0 1 1 1.493-.154 6.5 6.5 0 1 0 1.18-4.458l1.358 1.358A.25.25 0 0 1 3.896 6H.25A.25.25 0 0 1 0 5.75V2.104a.25.25 0 0 1 .427-.177ZM7.75 4a.75.75 0 0 1 .75.75v2.992l2.028.812a.75.75 0 0 1-.557 1.392l-2.5-1A.751.751 0 0 1 7 8.25v-3.5A.75.75 0 0 1 7.75 4Z"></path></svg></span></span></a></span></div></div></div></div></div><div class="Box-sc-g0xbh4-0 ldRxiI"><div class="Box-sc-g0xbh4-0 efRoCL container"><div class="Box-sc-g0xbh4-0 gNAmSV react-code-size-details-banner"><div class="Box-sc-g0xbh4-0 jNEwzY react-code-size-details-banner"><div class="Box-sc-g0xbh4-0 bsDwxw text-mono"><div title="9.07 KB" data-testid="blob-size" class="Truncate__StyledTruncate-sc-23o1d2-0 eAtkQz"><span>207 lines (164 loc) · 9.07 KB</span></div></div></div><div class="react-code-size-details-banner"><button style="--button-color:fg.default" type="button" aria-haspopup="true" aria-expanded="false" tabindex="0" data-testid="copilot-popover-button" class="Box-sc-g0xbh4-0 kXyYCF prc-Button-ButtonBase-c50BI" data-loading="false" data-size="small" data-variant="invisible" aria-describedby=":R15tal9lab:-loading-announcement" id=":R15tal9lab:"><span data-component="buttonContent" class="Box-sc-g0xbh4-0 gUkoLg prc-Button-ButtonContent-HKbr-"><span data-component="leadingVisual" class="prc-Button-Visual-2epfX prc-Button-VisualWrap-Db-eB"><svg aria-hidden="true" focusable="false" class="octicon octicon-copilot" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display:inline-block;user-select:none;vertical-align:text-bottom;overflow:visible"><path d="M7.998 15.035c-4.562 0-7.873-2.914-7.998-3.749V9.338c.085-.628.677-1.686 1.588-2.065.013-.07.024-.143.036-.218.029-.183.06-.384.126-.612-.201-.508-.254-1.084-.254-1.656 0-.87.128-1.769.693-2.484.579-.733 1.494-1.124 2.724-1.261 1.206-.134 2.262.034 2.944.765.05.053.096.108.139.165.044-.057.094-.112.143-.165.682-.731 1.738-.899 2.944-.765 1.23.137 2.145.528 2.724 1.261.566.715.693 1.614.693 2.484 0 .572-.053 1.148-.254 1.656.066.228.098.429.126.612.012.076.024.148.037.218.924.385 1.522 1.471 1.591 2.095v1.872c0 .766-3.351 3.795-8.002 3.795Zm0-1.485c2.28 0 4.584-1.11 5.002-1.433V7.862l-.023-.116c-.49.21-1.075.291-1.727.291-1.146 0-2.059-.327-2.71-.991A3.222 3.222 0 0 1 8 6.303a3.24 3.24 0 0 1-.544.743c-.65.664-1.563.991-2.71.991-.652 0-1.236-.081-1.727-.291l-.023.116v4.255c.419.323 2.722 1.433 5.002 1.433ZM6.762 2.83c-.193-.206-.637-.413-1.682-.297-1.019.113-1.479.404-1.713.7-.247.312-.369.789-.369 1.554 0 .793.129 1.171.308 1.371.162.181.519.379 1.442.379.853 0 1.339-.235 1.638-.54.315-.322.527-.827.617-1.553.117-.935-.037-1.395-.241-1.614Zm4.155-.297c-1.044-.116-1.488.091-1.681.297-.204.219-.359.679-.242 1.614.091.726.303 1.231.618 1.553.299.305.784.54 1.638.54.922 0 1.28-.198 1.442-.379.179-.2.308-.578.308-1.371 0-.765-.123-1.242-.37-1.554-.233-.296-.693-.587-1.713-.7Z"></path><path d="M6.25 9.037a.75.75 0 0 1 .75.75v1.501a.75.75 0 0 1-1.5 0V9.787a.75.75 0 0 1 .75-.75Zm4.25.75v1.501a.75.75 0 0 1-1.5 0V9.787a.75.75 0 0 1 1.5 0Z"></path></svg></span><span data-component="text" class="prc-Button-Label-pTQ3x">Code 55% faster with GitHub Copilot</span></span></button></div></div><div class="Box-sc-g0xbh4-0 jdLMhu react-blob-view-header-sticky" id="repos-sticky-header"><div class="Box-sc-g0xbh4-0 tOISc"><div class="react-blob-sticky-header"><div class="Box-sc-g0xbh4-0 hqwSEx"><div class="Box-sc-g0xbh4-0 lzKZY"><div class="Box-sc-g0xbh4-0 fHind"><nav data-testid="breadcrumbs" aria-labelledby="sticky-breadcrumb-heading" id="sticky-breadcrumb" class="Box-sc-g0xbh4-0 fzFXnm"><h2 class="sr-only prc-Heading-Heading-6CmGO" data-testid="screen-reader-heading" id="sticky-breadcrumb-heading">Breadcrumbs</h2><ol class="Box-sc-g0xbh4-0 iMnkmv"><li class="Box-sc-g0xbh4-0 ghzDag"><a class="Box-sc-g0xbh4-0 kHuKdh prc-Link-Link-85e08" sx="[object Object]" data-testid="breadcrumbs-repo-link" href="https://github.com/SumaikaImran/AI_LABS/tree/main">AI_LABS</a></li></ol></nav><div data-testid="breadcrumbs-filename" class="Box-sc-g0xbh4-0 ghzDag"><span class="Box-sc-g0xbh4-0 oDtgN prc-Text-Text-0ima0" aria-hidden="true">/</span><h1 class="Box-sc-g0xbh4-0 dnZoUW prc-Heading-Heading-6CmGO" tabindex="-1" id="sticky-file-name-id">app.py</h1></div></div><button style="--button-color:fg.default" type="button" class="Box-sc-g0xbh4-0 jRZWlf prc-Button-ButtonBase-c50BI" data-loading="false" data-size="small" data-variant="invisible" aria-describedby=":Riptal9lab:-loading-announcement"><span data-component="buttonContent" class="Box-sc-g0xbh4-0 gUkoLg prc-Button-ButtonContent-HKbr-"><span data-component="leadingVisual" class="prc-Button-Visual-2epfX prc-Button-VisualWrap-Db-eB"><svg aria-hidden="true" focusable="false" class="octicon octicon-arrow-up" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display:inline-block;user-select:none;vertical-align:text-bottom;overflow:visible"><path d="M3.47 7.78a.75.75 0 0 1 0-1.06l4.25-4.25a.75.75 0 0 1 1.06 0l4.25 4.25a.751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018L9 4.81v7.44a.75.75 0 0 1-1.5 0V4.81L4.53 7.78a.75.75 0 0 1-1.06 0Z"></path></svg></span><span data-component="text" class="prc-Button-Label-pTQ3x">Top</span></span></button></div></div></div><div class="Box-sc-g0xbh4-0 kTvpNk"><h2 class="sr-only prc-Heading-Heading-6CmGO" data-testid="screen-reader-heading">File metadata and controls</h2><div class="Box-sc-g0xbh4-0 iNMjfP"><ul aria-label="File view" class="SegmentedControl__SegmentedControlList-sc-1rzig82-0 lawgDG"><li class="Box-sc-g0xbh4-0 fefCSX"><button aria-current="true" type="button" class="SegmentedControlButton__SegmentedControlButtonStyled-sc-8lkgxl-0 dbGjOi" data-hotkey="Control+/ Control+c"><span class="segmentedControl-content"><div class="Box-sc-g0xbh4-0 segmentedControl-text">Code</div></span></button></li><li class="Box-sc-g0xbh4-0 idgUkN"><button aria-current="false" type="button" class="SegmentedControlButton__SegmentedControlButtonStyled-sc-8lkgxl-0 bHmvop" data-hotkey="b,Shift+B,Control+/ Control+b"><span class="segmentedControl-content"><div class="Box-sc-g0xbh4-0 segmentedControl-text">Blame</div></span></button></li></ul><button hidden="" data-testid="" data-hotkey-scope="read-only-cursor-text-area" data-hotkey="Control+/ Control+c"></button><button hidden="" data-testid="" data-hotkey-scope="read-only-cursor-text-area" data-hotkey="b,Shift+B,Control+/ Control+b"></button><div class="Box-sc-g0xbh4-0 jNEwzY react-code-size-details-in-header"><div class="Box-sc-g0xbh4-0 bsDwxw text-mono"><div title="9.07 KB" data-testid="blob-size" class="Truncate__StyledTruncate-sc-23o1d2-0 eAtkQz"><span>207 lines (164 loc) · 9.07 KB</span></div></div></div><div class="react-code-size-details-in-header"><button style="--button-color:fg.default" type="button" aria-haspopup="true" aria-expanded="false" tabindex="0" data-testid="copilot-popover-button" class="Box-sc-g0xbh4-0 kXyYCF prc-Button-ButtonBase-c50BI" data-loading="false" data-size="small" data-variant="invisible" aria-describedby=":R3kptal9lab:-loading-announcement" id=":R3kptal9lab:"><span data-component="buttonContent" class="Box-sc-g0xbh4-0 gUkoLg prc-Button-ButtonContent-HKbr-"><span data-component="leadingVisual" class="prc-Button-Visual-2epfX prc-Button-VisualWrap-Db-eB"><svg aria-hidden="true" focusable="false" class="octicon octicon-copilot" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display:inline-block;user-select:none;vertical-align:text-bottom;overflow:visible"><path d="M7.998 15.035c-4.562 0-7.873-2.914-7.998-3.749V9.338c.085-.628.677-1.686 1.588-2.065.013-.07.024-.143.036-.218.029-.183.06-.384.126-.612-.201-.508-.254-1.084-.254-1.656 0-.87.128-1.769.693-2.484.579-.733 1.494-1.124 2.724-1.261 1.206-.134 2.262.034 2.944.765.05.053.096.108.139.165.044-.057.094-.112.143-.165.682-.731 1.738-.899 2.944-.765 1.23.137 2.145.528 2.724 1.261.566.715.693 1.614.693 2.484 0 .572-.053 1.148-.254 1.656.066.228.098.429.126.612.012.076.024.148.037.218.924.385 1.522 1.471 1.591 2.095v1.872c0 .766-3.351 3.795-8.002 3.795Zm0-1.485c2.28 0 4.584-1.11 5.002-1.433V7.862l-.023-.116c-.49.21-1.075.291-1.727.291-1.146 0-2.059-.327-2.71-.991A3.222 3.222 0 0 1 8 6.303a3.24 3.24 0 0 1-.544.743c-.65.664-1.563.991-2.71.991-.652 0-1.236-.081-1.727-.291l-.023.116v4.255c.419.323 2.722 1.433 5.002 1.433ZM6.762 2.83c-.193-.206-.637-.413-1.682-.297-1.019.113-1.479.404-1.713.7-.247.312-.369.789-.369 1.554 0 .793.129 1.171.308 1.371.162.181.519.379 1.442.379.853 0 1.339-.235 1.638-.54.315-.322.527-.827.617-1.553.117-.935-.037-1.395-.241-1.614Zm4.155-.297c-1.044-.116-1.488.091-1.681.297-.204.219-.359.679-.242 1.614.091.726.303 1.231.618 1.553.299.305.784.54 1.638.54.922 0 1.28-.198 1.442-.379.179-.2.308-.578.308-1.371 0-.765-.123-1.242-.37-1.554-.233-.296-.693-.587-1.713-.7Z"></path><path d="M6.25 9.037a.75.75 0 0 1 .75.75v1.501a.75.75 0 0 1-1.5 0V9.787a.75.75 0 0 1 .75-.75Zm4.25.75v1.501a.75.75 0 0 1-1.5 0V9.787a.75.75 0 0 1 1.5 0Z"></path></svg></span><span data-component="text" class="prc-Button-Label-pTQ3x">Code 55% faster with GitHub Copilot</span></span></button></div></div><div class="Box-sc-g0xbh4-0 kcLCKF"><button hidden="" data-testid="" data-hotkey="Control+Shift+&gt;" data-hotkey-scope="read-only-cursor-text-area"></button><button hidden="" data-hotkey="Control+Shift+&gt;"></button><button hidden="" data-testid="" data-hotkey="Control+Shift+&lt;" data-hotkey-scope="read-only-cursor-text-area"></button><button hidden="" data-hotkey="Control+Shift+&lt;"></button><div class="Box-sc-g0xbh4-0 kVWtTz react-blob-header-edit-and-raw-actions"><div class="ButtonGroup__StyledButtonGroup-sc-1gxhls1-0 lirRhW"><a href="https://github.com/SumaikaImran/AI_LABS/raw/refs/heads/main/app.py" data-testid="raw-button" class="Box-sc-g0xbh4-0 gWqxTd prc-Button-ButtonBase-c50BI" data-loading="false" data-no-visuals="true" data-size="small" data-variant="default" aria-describedby=":R5csptal9lab:-loading-announcement" data-hotkey="Control+/ Control+r"><span data-component="buttonContent" class="Box-sc-g0xbh4-0 gUkoLg prc-Button-ButtonContent-HKbr-"><span data-component="text" class="prc-Button-Label-pTQ3x">Raw</span></span></a><button data-component="IconButton" type="button" aria-label="Copy raw content" data-testid="copy-raw-button" class="prc-Button-ButtonBase-c50BI prc-Button-IconButton-szpyj" data-loading="false" data-no-visuals="true" data-size="small" data-variant="default" aria-describedby=":Rpcsptal9lab:-loading-announcement" data-hotkey="Control+Shift+C"><svg aria-hidden="true" focusable="false" class="octicon octicon-copy" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display:inline-block;user-select:none;vertical-align:text-bottom;overflow:visible"><path d="M0 6.75C0 5.784.784 5 1.75 5h1.5a.75.75 0 0 1 0 1.5h-1.5a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-1.5a.75.75 0 0 1 1.5 0v1.5A1.75 1.75 0 0 1 9.25 16h-7.5A1.75 1.75 0 0 1 0 14.25Z"></path><path d="M5 1.75C5 .784 5.784 0 6.75 0h7.5C15.216 0 16 .784 16 1.75v7.5A1.75 1.75 0 0 1 14.25 11h-7.5A1.75 1.75 0 0 1 5 9.25Zm1.75-.25a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-7.5a.25.25 0 0 0-.25-.25Z"></path></svg></button><span role="tooltip" aria-label="Download raw file" id=":Rdcsptal9lab:" class="Tooltip__TooltipBase-sc-17tf59c-0 hWlpPn tooltipped-n"><button data-component="IconButton" type="button" aria-label="Download raw content" data-testid="download-raw-button" class="Box-sc-g0xbh4-0 ivobqY prc-Button-ButtonBase-c50BI prc-Button-IconButton-szpyj" data-loading="false" data-no-visuals="true" data-size="small" data-variant="default" aria-describedby=":Rtcsptal9lab:-loading-announcement" data-hotkey="Control+Shift+S"><svg aria-hidden="true" focusable="false" class="octicon octicon-download" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display:inline-block;user-select:none;vertical-align:text-bottom;overflow:visible"><path d="M2.75 14A1.75 1.75 0 0 1 1 12.25v-2.5a.75.75 0 0 1 1.5 0v2.5c0 .138.112.25.25.25h10.5a.25.25 0 0 0 .25-.25v-2.5a.75.75 0 0 1 1.5 0v2.5A1.75 1.75 0 0 1 13.25 14Z"></path><path d="M7.25 7.689V2a.75.75 0 0 1 1.5 0v5.689l1.97-1.969a.749.749 0 1 1 1.06 1.06l-3.25 3.25a.749.749 0 0 1-1.06 0L4.22 6.78a.749.749 0 1 1 1.06-1.06l1.97 1.969Z"></path></svg></button></span></div><button hidden="" data-testid="raw-button-shortcut" data-hotkey-scope="read-only-cursor-text-area" data-hotkey="Control+/ Control+r"></button><button hidden="" data-testid="copy-raw-button-shortcut" data-hotkey-scope="read-only-cursor-text-area" data-hotkey="Control+Shift+C"></button><button hidden="" data-testid="download-raw-button-shortcut" data-hotkey-scope="read-only-cursor-text-area" data-hotkey="Control+Shift+S"></button><a class="js-github-dev-shortcut d-none prc-Link-Link-85e08" href="https://github.dev/" data-hotkey="., Control+Shift+/"></a><button hidden="" data-testid="" data-hotkey-scope="read-only-cursor-text-area" data-hotkey="., Control+Shift+/"></button><a class="js-github-dev-new-tab-shortcut d-none prc-Link-Link-85e08" href="https://github.dev/" target="_blank" data-hotkey="Shift+.,Shift+&gt;,&gt;"></a><button hidden="" data-testid="" data-hotkey-scope="read-only-cursor-text-area" data-hotkey="Shift+.,Shift+&gt;,&gt;"></button><div class="ButtonGroup__StyledButtonGroup-sc-1gxhls1-0 lirRhW"><span role="tooltip" aria-label="Fork this repository and edit the file" id=":R6ksptal9lab:" class="Tooltip__TooltipBase-sc-17tf59c-0 hWlpPn tooltipped-nw"><a sx="[object Object]" data-component="IconButton" type="button" aria-label="Edit file" data-testid="edit-button" class="Box-sc-g0xbh4-0 kilKoS prc-Button-ButtonBase-c50BI prc-Button-IconButton-szpyj" data-loading="false" data-no-visuals="true" data-size="small" data-variant="default" aria-describedby=":Rmksptal9lab:-loading-announcement" href="https://github.com/SumaikaImran/AI_LABS/edit/main/app.py" data-hotkey="e,Shift+E"><svg aria-hidden="true" focusable="false" class="octicon octicon-pencil" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display:inline-block;user-select:none;vertical-align:text-bottom;overflow:visible"><path d="M11.013 1.427a1.75 1.75 0 0 1 2.474 0l1.086 1.086a1.75 1.75 0 0 1 0 2.474l-8.61 8.61c-.21.21-.47.364-.756.445l-3.251.93a.75.75 0 0 1-.927-.928l.929-3.25c.081-.286.235-.547.445-.758l8.61-8.61Zm.176 4.823L9.75 4.81l-6.286 6.287a.253.253 0 0 0-.064.108l-.558 1.953 1.953-.558a.253.253 0 0 0 .108-.064Zm1.238-3.763a.25.25 0 0 0-.354 0L10.811 3.75l1.439 1.44 1.263-1.263a.25.25 0 0 0 0-.354Z"></path></svg></a></span><button data-component="IconButton" type="button" aria-label="More edit options" data-testid="more-edit-button" aria-haspopup="true" aria-expanded="false" tabindex="0" class="prc-Button-ButtonBase-c50BI prc-Button-IconButton-szpyj" data-loading="false" data-no-visuals="true" data-size="small" data-variant="default" aria-describedby=":Raksptal9lab:-loading-announcement" id=":Raksptal9lab:"><svg aria-hidden="true" focusable="false" class="octicon octicon-triangle-down" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display:inline-block;user-select:none;vertical-align:text-bottom;overflow:visible"><path d="m4.427 7.427 3.396 3.396a.25.25 0 0 0 .354 0l3.396-3.396A.25.25 0 0 0 11.396 7H4.604a.25.25 0 0 0-.177.427Z"></path></svg></button></div><button hidden="" data-testid="" data-hotkey="e,Shift+E" data-hotkey-scope="read-only-cursor-text-area"></button></div><span role="tooltip" aria-label="Close symbols panel" id=":R5sptal9lab:" class="Tooltip__TooltipBase-sc-17tf59c-0 hWlpPn tooltipped-nw"><button data-component="IconButton" type="button" aria-label="Symbols" aria-pressed="true" aria-expanded="true" aria-controls="symbols-pane" data-testid="symbols-button" class="Box-sc-g0xbh4-0 heuRGy prc-Button-ButtonBase-c50BI prc-Button-IconButton-szpyj" data-loading="false" data-no-visuals="true" data-size="small" data-variant="invisible" aria-describedby="symbols-button-loading-announcement" id="symbols-button" data-hotkey="Control+i"><svg aria-hidden="true" focusable="false" class="octicon octicon-code-square" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display:inline-block;user-select:none;vertical-align:text-bottom;overflow:visible"><path d="M0 1.75C0 .784.784 0 1.75 0h12.5C15.216 0 16 .784 16 1.75v12.5A1.75 1.75 0 0 1 14.25 16H1.75A1.75 1.75 0 0 1 0 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h12.5a.25.25 0 0 0 .25-.25V1.75a.25.25 0 0 0-.25-.25Zm7.47 3.97a.75.75 0 0 1 1.06 0l2 2a.75.75 0 0 1 0 1.06l-2 2a.749.749 0 0 1-1.275-.326.749.749 0 0 1 .215-.734L10.69 8 9.22 6.53a.75.75 0 0 1 0-1.06ZM6.78 6.53 5.31 8l1.47 1.47a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215l-2-2a.75.75 0 0 1 0-1.06l2-2a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042Z"></path></svg></button></span><div class="react-blob-header-edit-and-raw-actions-combined"><button data-component="IconButton" type="button" aria-label="Edit and raw actions" title="More file actions" data-testid="more-file-actions-button" aria-haspopup="true" aria-expanded="false" tabindex="0" class="Box-sc-g0xbh4-0 ffkqe prc-Button-ButtonBase-c50BI js-blob-dropdown-click prc-Button-IconButton-szpyj" data-loading="false" data-no-visuals="true" data-size="small" data-variant="invisible" aria-describedby=":Rnsptal9lab:-loading-announcement" id=":Rnsptal9lab:"><svg aria-hidden="true" focusable="false" class="octicon octicon-kebab-horizontal" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display:inline-block;user-select:none;vertical-align:text-bottom;overflow:visible"><path d="M8 9a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3ZM1.5 9a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Zm13 0a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Z"></path></svg></button></div></div></div></div><div></div></div><div class="Box-sc-g0xbh4-0 hGyMdv"><section aria-labelledby="file-name-id-wide file-name-id-mobile" class="Box-sc-g0xbh4-0 dceWRL"><div class="Box-sc-g0xbh4-0 dGXHv"><div id="highlighted-line-menu-positioner" class="position-relative"><div id="copilot-button-positioner" class="Box-sc-g0xbh4-0 bpDFns"><div class="Box-sc-g0xbh4-0 iJOeCH"><div class="Box-sc-g0xbh4-0 eJSJhL"><div class="Box-sc-g0xbh4-0 kngVFz"><div aria-hidden="true" data-testid="navigation-cursor" class="Box-sc-g0xbh4-0 code-navigation-cursor" style="top: 0px; left: 92px;"> </div><button hidden="" data-testid="NavigationCursorEnter" data-hotkey="Control+Enter" data-hotkey-scope="read-only-cursor-text-area"></button><button hidden="" data-testid="NavigationCursorSetHighlightedLine" data-hotkey="Shift+J" data-hotkey-scope="read-only-cursor-text-area"></button><button hidden="" data-testid="NavigationCursorSetHighlightAndExpandMenu" data-hotkey="Alt+Shift+C,Alt+Shift+Ç" data-hotkey-scope="read-only-cursor-text-area"></button><button hidden="" data-testid="NavigationCursorPageDown" data-hotkey="PageDown" data-hotkey-scope="read-only-cursor-text-area"></button><button hidden="" data-testid="NavigationCursorPageUp" data-hotkey="PageUp" data-hotkey-scope="read-only-cursor-text-area"></button><button hidden="" data-testid="" data-hotkey="/" data-hotkey-scope="read-only-cursor-text-area"></button></div></div><textarea id="read-only-cursor-text-area" data-testid="read-only-cursor-text-area" aria-label="file content" aria-readonly="true" inputmode="none" tabindex="0" aria-multiline="true" aria-haspopup="false" data-gramm="false" data-gramm_editor="false" data-enable-grammarly="false" spellcheck="false" autocorrect="off" autocapitalize="off" autocomplete="off" data-ms-editor="false" class="react-blob-textarea react-blob-print-hide" style="resize: none; margin-top: -2px; padding-left: 92px; padding-right: 70px; width: 100%; background-color: unset; box-sizing: border-box; color: transparent; position: absolute; border: none; tab-size: 8; outline: none; overflow: auto hidden; height: 4160px; font-size: 12px; line-height: 20px; overflow-wrap: normal; overscroll-behavior-x: none; white-space: pre; z-index: 1;">
from flask import Flask, render_template, request

app = Flask(__name__)

# Route for the main page
@app.route('/')
def index():
    return render_template('index.html')

# Route to generate a surgery schedule based on input
@app.route('/generate_schedule', methods=['POST'])
def generate_schedule():
    try:
        # Get the input values from the form
        num_surgeries = int(request.form['num_surgeries'])
        num_rooms = int(request.form['num_rooms'])
        num_staff = int(request.form['num_staff'])

        # Get the durations of each surgery
        durations = [int(request.form[f'duration_{i+1}']) for i in range(num_surgeries)]

        # Get staff skills for each surgery
        staff_skills = []
        for i in range(num_surgeries):
            skills = [
                int(request.form.get(f'surgery_{i+1}_staff_{j+1}', 0)) 
                for j in range(1, num_staff + 1)
            ] 
            '''request.forms.get Retrieves the value of the form input corresponding to whether staff member j is available for surgery i+1.
Example: If i = 0 (first surgery) and j = 1 (first staff member), it looks for the input field with the name surgery_1_staff_1.
The default value is 0, meaning if the input is missing, it assumes that the staff member is unavailable for that surgery.'''
#Collect the skills (binary values: 0 or 1) of all staff members for the current surgery
            staff_skills.append(skills)
            '''skills is a list Each row corresponds to a surgery.
Each element in a row is 0 or 1, indicating whether a specific staff member is available for that surgery.'''

        # Generate the schedule using the genetic algorithm
        schedule = genetic_algorithm(num_surgeries, num_rooms, num_staff, durations, staff_skills)

 
        """
            If no valid schedule is generated, display an error message.
             This may occur if inputs are inconsistent or constraints cannot be satisfied.
             """
        if not schedule:
            error = "No valid schedule could be generated. Please check the inputs and try again."
            return render_template('index.html', error=error)
        
        # Render the schedule on the page
        return render_template('index.html', schedule=schedule)

    except Exception as e:
        # Handle errors gracefully and display the error message
        return render_template('index.html', error=f"An error occurred: {e}")

# Genetic Algorithm for generating an optimal surgery schedule
def genetic_algorithm(num_surgeries, num_rooms, num_staff, durations, staff_skills, slot_duration=40, max_room_slots=7):
    import random
# Genetic Algorithm to generate an optimal schedule for surgeries.
    
#     Parameters:
#         num_surgeries (int): Total number of surgeries to schedule.
#         num_rooms (int): Number of available operating rooms.
#         num_staff (int): Total staff members available.
#         durations (list): List of surgery durations.
#         staff_skills (list): 2D list indicating staff eligibility for each surgery.
#         slot_duration (int): Duration of each time slot in minutes (default: 40).
#         max_room_slots (int): Maximum time slots available per room (default: 7).
    # Calculate the number of slots required for each surgery
    # (divide surgery duration by slot duration, rounding up for partial slots)
   # Returns:
#         list: A schedule containing surgery details or None if no valid schedule is found.
    slots_required = [(-(-dur // slot_duration)) for dur in durations] 
    
    #to perform ceiling division using integer arithmetic
    '''Floor division (//) truncates toward zero, while ceiling division needs to round up.
Negating the number "reverses" the truncation direction of //, effectively performing a ceiling operation.(-(-50 // 40))  # Perform step by step
= -((-50) // 40)
= -(-2)  # -50 divided by 40 is -1.25, floored to -2
= 2  '''

    # Validate staff availability for each surgery
    valid_staff = []
    for i in range(num_surgeries):
        """
       Collect a list of staff members eligible for each surgery.
         If no staff is available for a surgery, return None to indicate an invalid schedule.
         """
        staff_for_surgery = [s + 1 for s, can_do in enumerate(staff_skills[i]) ]
        if not staff_for_surgery:
            return None  # If no staff is available for a surgery, return an invalid schedule
        valid_staff.append(staff_for_surgery)

    # Step 1: Initialize the population with random schedules
    population = []
    for _ in range(50):  # Population size of 50
        """
       Create a random schedule for each individual in the population.
         Assign surgeries to random rooms, time slots, and eligible staff members.
         """
        individual = []
        for i in range(num_surgeries):
            room = random.randint(1, num_rooms)  # Assign a random room
            start_slot = random.randint(1, max_room_slots - slots_required[i] + 1)  # Assign a random starting slot
            assigned_staff = random.sample(valid_staff[i], k=1)  # Randomly assign at least one valid staff member
            individual.append({
                "surgery": i + 1, 
                "room": room,  # Assigned room
                "start_slot": start_slot,  # Starting time slot
                "end_slot": start_slot + slots_required[i] - 1,  # Ending time slot
                "staff": assigned_staff  # Assigned staff members
            })
        population.append(individual)

    # Fitness Function: Evaluate the quality of a schedule
    def fitness(individual):

        """
        Calculate the fitness of a schedule.
        
        Parameters:
            individual (list): A schedule (list of surgeries with room, time slot, and staff assignments).
        
        Returns:
            int: A fitness score based on overlap and staff assignment validity.
        """
        score = 0
        room_schedule = {room: [] for room in range(1, num_rooms + 1)}  # Track room schedules

        for surgery in individual:
            room = surgery["room"]
            start = surgery["start_slot"]
            end = surgery["end_slot"]

            # Penalize overlapping surgeries in the same room
            for booked in room_schedule[room]:
                if not (end &lt; booked[0] or start &gt; booked[1]):  # Overlap detected
                    score -= 10

            # Penalize invalid staff assignments
            for staff in surgery["staff"]:
                if staff not in valid_staff[surgery["surgery"] - 1]:
                    score -= 1   #changed from 15

            # Update the room's schedule
            room_schedule[room].append((start, end))
            score += 1  # Reward valid room and staff assignments changed from 5 to 1

        return score

    # Evolution Function: Create the next generation of schedules
    def evolve(population):
        
        # Sort the population by fitness (higher is better)
        population.sort(key=lambda x: fitness(x), reverse=True)

        # Select the top 10 schedules as parents for the next generation
        new_population = population[:10]

        # Generate new individuals by crossover and mutation until the population is full
        while len(new_population) &lt; 50:
            # Select two parents from the top 10 fittest schedules
            p1, p2 = random.sample(population[:10], 2)

            # Perform crossover by combining parts of the parents
            crossover_point = random.randint(0, num_surgeries - 1)
            child = p1[:crossover_point] + p2[crossover_point:]

            # Mutation: Randomly adjust room or starting slot for some surgeries
            if random.random() &lt; 0.01:  # 1% chance of mutation
                idx = random.randint(0, num_surgeries - 1)  # Select a random surgery to mutate
                child[idx]["room"] = random.randint(1, num_rooms)  # Assign a new random room
                child[idx]["start_slot"] = random.randint(1, max_room_slots - slots_required[idx] + 1)  # Assign a new random start slot

            # Add the mutated child to the new population
            new_population.append(child)

        return new_population

    # Step 2: Run the genetic algorithm for a fixed number of generations
    for _ in range(50):  # Run for 50 generations
        population = evolve(population)  # Evolve the population

    # Step 3: Select the best schedule from the final generation
    best_schedule = max(population, key=lambda x: fitness(x))

    # Format the best schedule for display
    final_schedule = []
    for surgery in best_schedule:
        final_schedule.append({
            "surgery": surgery["surgery"],
            "room": surgery["room"],
            "slots": f"{surgery['start_slot']} - {surgery['end_slot']}",
            "staff": ', '.join(map(str, surgery["staff"])) if surgery["staff"] else "No Staff Assigned"
        })

    return final_schedule

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)




        </textarea><button hidden="" data-testid="" data-hotkey="Alt+F1,Control+Alt+˙,Control+Alt+h" data-hotkey-scope="read-only-cursor-text-area"></button><div class="Box-sc-g0xbh4-0 kHHiZS"><div tabindex="0" class="Box-sc-g0xbh4-0 jqUoVd"><div class="Box-sc-g0xbh4-0 eOLJKp react-code-file-contents" role="presentation" aria-hidden="true" data-tab-size="8" data-testid="code-lines-container" data-paste-markdown-skip="true" data-hpc="true" style="height: 4140px;"><div class="react-line-numbers" style="pointer-events: auto; height: 4140px; position: relative; z-index: 2;"><div data-line-number="1" class="react-line-number react-code-text" style="padding-right: 16px;">1</div><div data-line-number="2" class="react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(20px);">2</div><div data-line-number="3" class="react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(40px);">3</div><div data-line-number="4" class="react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(60px);">4</div><div data-line-number="5" class="react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(80px);">5</div><div data-line-number="6" class="react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(100px);">6</div><div data-line-number="7" class="react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(120px);">7</div><div data-line-number="8" class="react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(140px);">8</div><div data-line-number="9" class="react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(160px);">9</div><div data-line-number="10" class="react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(180px);">10</div><div data-line-number="11" class="react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(200px);">11</div><div data-line-number="12" class="react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(220px);">12</div><div data-line-number="13" class="react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(240px);">13<span class="Box-sc-g0xbh4-0 cJGaMs"><div aria-label="Collapse code section" role="button" class="Box-sc-g0xbh4-0 iGLarr"><svg aria-hidden="true" focusable="false" class="Octicon-sc-9kayk9-0" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display: inline-block; user-select: none; vertical-align: text-bottom; overflow: visible;"><path d="M12.78 5.22a.749.749 0 0 1 0 1.06l-4.25 4.25a.749.749 0 0 1-1.06 0L3.22 6.28a.749.749 0 1 1 1.06-1.06L8 8.939l3.72-3.719a.749.749 0 0 1 1.06 0Z"></path></svg></div></span></div><div data-line-number="14" class="child-of-line-12  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(260px);">14</div><div data-line-number="15" class="child-of-line-12  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(280px);">15</div><div data-line-number="16" class="child-of-line-12  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(300px);">16</div><div data-line-number="17" class="child-of-line-12  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(320px);">17</div><div data-line-number="18" class="child-of-line-12  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(340px);">18</div><div data-line-number="19" class="child-of-line-12  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(360px);">19</div><div data-line-number="20" class="child-of-line-12  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(380px);">20</div><div data-line-number="21" class="child-of-line-12  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(400px);">21</div><div data-line-number="22" class="child-of-line-12  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(420px);">22</div><div data-line-number="23" class="child-of-line-12  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(440px);">23</div><div data-line-number="24" class="child-of-line-12  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(460px);">24</div><div data-line-number="25" class="child-of-line-12  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(480px);">25</div><div data-line-number="26" class="child-of-line-12  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(500px);">26</div><div data-line-number="27" class="child-of-line-12  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(520px);">27</div><div data-line-number="28" class="child-of-line-12  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(540px);">28</div><div data-line-number="29" class="child-of-line-12  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(560px);">29</div><div data-line-number="30" class="child-of-line-12  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(580px);">30</div><div data-line-number="31" class="child-of-line-12  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(600px);">31</div><div data-line-number="32" class="child-of-line-12  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(620px);">32</div><div data-line-number="33" class="child-of-line-12  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(640px);">33</div><div data-line-number="34" class="child-of-line-12  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(660px);">34</div><div data-line-number="35" class="child-of-line-12  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(680px);">35</div><div data-line-number="36" class="child-of-line-12  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(700px);">36</div><div data-line-number="37" class="child-of-line-12  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(720px);">37</div><div data-line-number="38" class="child-of-line-12  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(740px);">38</div><div data-line-number="39" class="child-of-line-12  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(760px);">39</div><div data-line-number="40" class="child-of-line-12  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(780px);">40</div><div data-line-number="41" class="child-of-line-12  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(800px);">41</div><div data-line-number="42" class="child-of-line-12  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(820px);">42</div><div data-line-number="43" class="child-of-line-12  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(840px);">43</div><div data-line-number="44" class="child-of-line-12  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(860px);">44</div><div data-line-number="45" class="child-of-line-12  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(880px);">45</div><div data-line-number="46" class="child-of-line-12  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(900px);">46</div><div data-line-number="47" class="child-of-line-12  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(920px);">47</div><div data-line-number="48" class="child-of-line-12  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(940px);">48</div><div data-line-number="49" class="child-of-line-12  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(960px);">49</div><div data-line-number="50" class="child-of-line-12  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(980px);">50</div><div data-line-number="51" class="child-of-line-12  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(1000px);">51</div><div data-line-number="52" class="child-of-line-12  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(1020px);">52</div><div data-line-number="53" class="child-of-line-12  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(1040px);">53</div><div data-line-number="54" class="child-of-line-12  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(1060px);">54</div><div data-line-number="55" class="react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(1080px);">55</div><div data-line-number="56" class="react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(1100px);">56</div><div data-line-number="57" class="react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(1120px);">57</div><div data-line-number="58" class="react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(1140px);">58<span class="Box-sc-g0xbh4-0 cJGaMs"><div aria-label="Collapse code section" role="button" class="Box-sc-g0xbh4-0 iGLarr"><svg aria-hidden="true" focusable="false" class="Octicon-sc-9kayk9-0" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display: inline-block; user-select: none; vertical-align: text-bottom; overflow: visible;"><path d="M12.78 5.22a.749.749 0 0 1 0 1.06l-4.25 4.25a.749.749 0 0 1-1.06 0L3.22 6.28a.749.749 0 1 1 1.06-1.06L8 8.939l3.72-3.719a.749.749 0 0 1 1.06 0Z"></path></svg></div></span></div><div data-line-number="59" class="child-of-line-57  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(1160px);">59</div><div data-line-number="60" class="child-of-line-57  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(1180px);">60</div><div data-line-number="61" class="child-of-line-57  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(1200px);">61</div><div data-line-number="62" class="child-of-line-57  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(1220px);">62</div><div data-line-number="63" class="child-of-line-57  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(1240px);">63</div><div data-line-number="64" class="child-of-line-57  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(1260px);">64</div><div data-line-number="65" class="child-of-line-57  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(1280px);">65</div><div data-line-number="66" class="child-of-line-57  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(1300px);">66</div><div data-line-number="67" class="child-of-line-57  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(1320px);">67</div><div data-line-number="68" class="child-of-line-57  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(1340px);">68</div><div data-line-number="69" class="child-of-line-57  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(1360px);">69</div><div data-line-number="70" class="child-of-line-57  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(1380px);">70</div><div data-line-number="71" class="child-of-line-57  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(1400px);">71</div><div data-line-number="72" class="child-of-line-57  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(1420px);">72</div><div data-line-number="73" class="child-of-line-57  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(1440px);">73</div><div data-line-number="74" class="child-of-line-57  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(1460px);">74</div><div data-line-number="75" class="child-of-line-57  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(1480px);">75</div><div data-line-number="76" class="child-of-line-57  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(1500px);">76</div><div data-line-number="77" class="child-of-line-57  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(1520px);">77</div><div data-line-number="78" class="child-of-line-57  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(1540px);">78</div><div data-line-number="79" class="child-of-line-57  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(1560px);">79</div><div data-line-number="80" class="child-of-line-57  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(1580px);">80</div><div data-line-number="81" class="child-of-line-57  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(1600px);">81</div><div data-line-number="82" class="child-of-line-57  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(1620px);">82</div><div data-line-number="83" class="child-of-line-57  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(1640px);">83</div><div data-line-number="84" class="child-of-line-57  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(1660px);">84</div><div data-line-number="85" class="child-of-line-57  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(1680px);">85</div><div data-line-number="86" class="child-of-line-57  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(1700px);">86</div><div data-line-number="87" class="child-of-line-57  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(1720px);">87</div><div data-line-number="88" class="child-of-line-57  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(1740px);">88</div><div data-line-number="89" class="child-of-line-57  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(1760px);">89</div><div data-line-number="90" class="child-of-line-57  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(1780px);">90</div><div data-line-number="91" class="child-of-line-57  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(1800px);">91</div><div data-line-number="92" class="child-of-line-57  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(1820px);">92</div><div data-line-number="93" class="child-of-line-57  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(1840px);">93</div><div data-line-number="94" class="child-of-line-57  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(1860px);">94</div><div data-line-number="95" class="child-of-line-57  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(1880px);">95</div><div data-line-number="96" class="child-of-line-57  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(1900px);">96</div><div data-line-number="97" class="child-of-line-57  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(1920px);">97</div><div data-line-number="98" class="child-of-line-57  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(1940px);">98</div><div data-line-number="99" class="child-of-line-57  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(1960px);">99</div><div data-line-number="100" class="child-of-line-57  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(1980px);">100</div><div data-line-number="101" class="child-of-line-57  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(2000px);">101</div><div data-line-number="102" class="child-of-line-57  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(2020px);">102</div><div data-line-number="103" class="child-of-line-57  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(2040px);">103</div><div data-line-number="104" class="child-of-line-57  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(2060px);">104</div><div data-line-number="105" class="child-of-line-57  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(2080px);">105</div><div data-line-number="106" class="child-of-line-57  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(2100px);">106</div><div data-line-number="107" class="child-of-line-57  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(2120px);">107</div><div data-line-number="108" class="child-of-line-57  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(2140px);">108</div><div data-line-number="109" class="child-of-line-57  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(2160px);">109</div><div data-line-number="110" class="child-of-line-57  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(2180px);">110</div><div data-line-number="111" class="child-of-line-57  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(2200px);">111</div><div data-line-number="112" class="child-of-line-57  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(2220px);">112</div><div data-line-number="113" class="child-of-line-57  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(2240px);">113</div><div data-line-number="114" class="child-of-line-57  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(2260px);">114</div><div data-line-number="115" class="child-of-line-57  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(2280px);">115</div><div data-line-number="116" class="child-of-line-57  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(2300px);">116</div><div data-line-number="117" class="child-of-line-57  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(2320px);">117<span class="Box-sc-g0xbh4-0 cJGaMs"><div aria-label="Collapse code section" role="button" class="Box-sc-g0xbh4-0 iGLarr"><svg aria-hidden="true" focusable="false" class="Octicon-sc-9kayk9-0" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display: inline-block; user-select: none; vertical-align: text-bottom; overflow: visible;"><path d="M12.78 5.22a.749.749 0 0 1 0 1.06l-4.25 4.25a.749.749 0 0 1-1.06 0L3.22 6.28a.749.749 0 1 1 1.06-1.06L8 8.939l3.72-3.719a.749.749 0 0 1 1.06 0Z"></path></svg></div></span></div><div data-line-number="118" class="child-of-line-57 child-of-line-116  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(2340px);">118</div><div data-line-number="134" class="child-of-line-57 child-of-line-116  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(2660px);">134</div><div data-line-number="135" class="child-of-line-57 child-of-line-116  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(2680px);">135</div><div data-line-number="136" class="child-of-line-57 child-of-line-116  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(2700px);">136</div><div data-line-number="137" class="child-of-line-57 child-of-line-116  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(2720px);">137</div><div data-line-number="138" class="child-of-line-57 child-of-line-116  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(2740px);">138</div><div data-line-number="139" class="child-of-line-57 child-of-line-116  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(2760px);">139</div><div data-line-number="140" class="child-of-line-57 child-of-line-116  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(2780px);">140</div><div data-line-number="141" class="child-of-line-57 child-of-line-116  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(2800px);">141</div><div data-line-number="142" class="child-of-line-57 child-of-line-116  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(2820px);">142</div><div data-line-number="143" class="child-of-line-57 child-of-line-116  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(2840px);">143</div><div data-line-number="144" class="child-of-line-57 child-of-line-116  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(2860px);">144</div><div data-line-number="145" class="child-of-line-57 child-of-line-116  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(2880px);">145</div><div data-line-number="146" class="child-of-line-57 child-of-line-116  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(2900px);">146</div><div data-line-number="147" class="child-of-line-57 child-of-line-116  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(2920px);">147</div><div data-line-number="148" class="child-of-line-57 child-of-line-116  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(2940px);">148</div><div data-line-number="149" class="child-of-line-57 child-of-line-116  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(2960px);">149</div><div data-line-number="150" class="child-of-line-57  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(2980px);">150</div><div data-line-number="151" class="child-of-line-57  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(3000px);">151</div><div data-line-number="152" class="child-of-line-57  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(3020px);">152</div><div data-line-number="153" class="child-of-line-57  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(3040px);">153<span class="Box-sc-g0xbh4-0 cJGaMs"><div aria-label="Collapse code section" role="button" class="Box-sc-g0xbh4-0 iGLarr"><svg aria-hidden="true" focusable="false" class="Octicon-sc-9kayk9-0" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display: inline-block; user-select: none; vertical-align: text-bottom; overflow: visible;"><path d="M12.78 5.22a.749.749 0 0 1 0 1.06l-4.25 4.25a.749.749 0 0 1-1.06 0L3.22 6.28a.749.749 0 1 1 1.06-1.06L8 8.939l3.72-3.719a.749.749 0 0 1 1.06 0Z"></path></svg></div></span></div><div data-line-number="154" class="child-of-line-57 child-of-line-152  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(3060px);">154</div><div data-line-number="155" class="child-of-line-57 child-of-line-152  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(3080px);">155</div><div data-line-number="156" class="child-of-line-57 child-of-line-152  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(3100px);">156</div><div data-line-number="157" class="child-of-line-57 child-of-line-152  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(3120px);">157</div><div data-line-number="158" class="child-of-line-57 child-of-line-152  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(3140px);">158</div><div data-line-number="159" class="child-of-line-57 child-of-line-152  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(3160px);">159</div><div data-line-number="160" class="child-of-line-57 child-of-line-152  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(3180px);">160</div><div data-line-number="161" class="child-of-line-57 child-of-line-152  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(3200px);">161</div><div data-line-number="162" class="child-of-line-57 child-of-line-152  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(3220px);">162</div><div data-line-number="163" class="child-of-line-57 child-of-line-152  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(3240px);">163</div><div data-line-number="164" class="child-of-line-57 child-of-line-152  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(3260px);">164</div><div data-line-number="165" class="child-of-line-57 child-of-line-152  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(3280px);">165</div><div data-line-number="166" class="child-of-line-57 child-of-line-152  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(3300px);">166</div><div data-line-number="167" class="child-of-line-57 child-of-line-152  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(3320px);">167</div><div data-line-number="168" class="child-of-line-57 child-of-line-152  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(3340px);">168</div><div data-line-number="169" class="child-of-line-57 child-of-line-152  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(3360px);">169</div><div data-line-number="170" class="child-of-line-57 child-of-line-152  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(3380px);">170</div><div data-line-number="171" class="child-of-line-57 child-of-line-152  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(3400px);">171</div><div data-line-number="172" class="child-of-line-57 child-of-line-152  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(3420px);">172</div><div data-line-number="173" class="child-of-line-57 child-of-line-152  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(3440px);">173</div><div data-line-number="174" class="child-of-line-57 child-of-line-152  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(3460px);">174</div><div data-line-number="175" class="child-of-line-57 child-of-line-152  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(3480px);">175</div><div data-line-number="176" class="child-of-line-57 child-of-line-152  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(3500px);">176</div><div data-line-number="177" class="child-of-line-57 child-of-line-152  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(3520px);">177</div><div data-line-number="178" class="child-of-line-57 child-of-line-152  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(3540px);">178</div><div data-line-number="179" class="child-of-line-57  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(3560px);">179</div><div data-line-number="180" class="child-of-line-57  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(3580px);">180</div><div data-line-number="181" class="child-of-line-57  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(3600px);">181</div><div data-line-number="182" class="child-of-line-57  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(3620px);">182</div><div data-line-number="183" class="child-of-line-57  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(3640px);">183</div><div data-line-number="184" class="child-of-line-57  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(3660px);">184</div><div data-line-number="185" class="child-of-line-57  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(3680px);">185</div><div data-line-number="186" class="child-of-line-57  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(3700px);">186</div><div data-line-number="187" class="child-of-line-57  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(3720px);">187</div><div data-line-number="188" class="child-of-line-57  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(3740px);">188</div><div data-line-number="189" class="child-of-line-57  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(3760px);">189</div><div data-line-number="190" class="child-of-line-57  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(3780px);">190</div><div data-line-number="191" class="child-of-line-57  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(3800px);">191</div><div data-line-number="192" class="child-of-line-57  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(3820px);">192</div><div data-line-number="193" class="child-of-line-57  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(3840px);">193</div><div data-line-number="194" class="child-of-line-57  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(3860px);">194</div><div data-line-number="195" class="child-of-line-57  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(3880px);">195</div><div data-line-number="196" class="child-of-line-57  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(3900px);">196</div><div data-line-number="197" class="child-of-line-57  react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(3920px);">197</div><div data-line-number="198" class="react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(3940px);">198</div><div data-line-number="199" class="react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(3960px);">199</div><div data-line-number="200" class="react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(3980px);">200</div><div data-line-number="201" class="react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(4000px);">201</div><div data-line-number="202" class="react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(4020px);">202</div><div data-line-number="203" class="react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(4040px);">203</div><div data-line-number="204" class="react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(4060px);">204</div><div data-line-number="205" class="react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(4080px);">205</div><div data-line-number="206" class="react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(4100px);">206</div><div data-line-number="207" class="react-line-number react-code-text virtual" style="padding-right: 16px; transform: translateY(4120px);">207</div></div><div class="react-code-lines" style="height: 4140px;"><div data-key="0" class="react-code-text react-code-line-contents" style="min-height: auto;"><div><div id="LC1" class="react-file-line html-div" data-testid="code-cell" data-line-number="1" inert="inert" style="position: relative;">
</div></div></div><div data-key="1" class="react-code-text react-code-line-contents virtual" style="transform: translateY(20px); min-height: auto;"><div><div id="LC2" class="react-file-line html-div" data-testid="code-cell" data-line-number="2" inert="inert" style="position: relative;"><span class="pl-k">from</span> <span class="pl-s1">flask</span> <span class="pl-k">import</span> <span class="pl-v">Flask</span>, <span class="pl-s1">render_template</span>, <span class="pl-s1">request</span></div></div></div><div data-key="2" class="react-code-text react-code-line-contents virtual" style="transform: translateY(40px); min-height: auto;"><div><div id="LC3" class="react-file-line html-div" data-testid="code-cell" data-line-number="3" inert="inert" style="position: relative;">
</div></div></div><div data-key="3" class="react-code-text react-code-line-contents virtual" style="transform: translateY(60px); min-height: auto;"><div><div id="LC4" class="react-file-line html-div" data-testid="code-cell" data-line-number="4" inert="inert" style="position: relative;"><span class="pl-s1">app</span> <span class="pl-c1">=</span> <span class="pl-v">Flask</span>(<span class="pl-s1">__name__</span>)</div></div></div><div data-key="4" class="react-code-text react-code-line-contents virtual" style="transform: translateY(80px); min-height: auto;"><div><div id="LC5" class="react-file-line html-div" data-testid="code-cell" data-line-number="5" inert="inert" style="position: relative;">
</div></div></div><div data-key="5" class="react-code-text react-code-line-contents virtual" style="transform: translateY(100px); min-height: auto;"><div><div id="LC6" class="react-file-line html-div" data-testid="code-cell" data-line-number="6" inert="inert" style="position: relative;"><span class="pl-c"># Route for the main page</span></div></div></div><div data-key="6" class="react-code-text react-code-line-contents virtual" style="transform: translateY(120px); min-height: auto;"><div><div id="LC7" class="react-file-line html-div" data-testid="code-cell" data-line-number="7" inert="inert" style="position: relative;"><span class="pl-en">@<span class="pl-s1">app</span>.<span class="pl-en">route</span>(<span class="pl-s">'/'</span>)</span></div></div></div><div data-key="7" class="react-code-text react-code-line-contents virtual" style="transform: translateY(140px); min-height: auto;"><div><div id="LC8" class="react-file-line html-div" data-testid="code-cell" data-line-number="8" inert="inert" style="position: relative;"><span class="pl-k">def</span> <span class="pl-en">index</span>():</div></div></div><div data-key="8" class="react-code-text react-code-line-contents virtual" style="transform: translateY(160px); min-height: auto;"><div><div id="LC9" class="react-file-line html-div" data-testid="code-cell" data-line-number="9" inert="inert" style="position: relative;">    <span class="pl-k">return</span> <span class="pl-en">render_template</span>(<span class="pl-s">'index.html'</span>)</div></div></div><div data-key="9" class="react-code-text react-code-line-contents virtual" style="transform: translateY(180px); min-height: auto;"><div><div id="LC10" class="react-file-line html-div" data-testid="code-cell" data-line-number="10" inert="inert" style="position: relative;">
</div></div></div><div data-key="10" class="react-code-text react-code-line-contents virtual" style="transform: translateY(200px); min-height: auto;"><div><div id="LC11" class="react-file-line html-div" data-testid="code-cell" data-line-number="11" inert="inert" style="position: relative;"><span class="pl-c"># Route to generate a surgery schedule based on input</span></div></div></div><div data-key="11" class="react-code-text react-code-line-contents virtual" style="transform: translateY(220px); min-height: auto;"><div><div id="LC12" class="react-file-line html-div" data-testid="code-cell" data-line-number="12" inert="inert" style="position: relative;"><span class="pl-en">@<span class="pl-s1">app</span>.<span class="pl-en">route</span>(<span class="pl-s">'/generate_schedule'</span>, <span class="pl-s1">methods</span><span class="pl-c1">=</span>[<span class="pl-s">'POST'</span>])</span></div></div></div><div data-key="12" class="react-code-text react-code-line-contents virtual" style="transform: translateY(240px); min-height: auto;"><div><div id="LC13" class="react-file-line html-div" data-testid="code-cell" data-line-number="13" inert="inert" style="position: relative;"><span class="pl-k">def</span> <span class="pl-en">generate_schedule</span>():</div></div></div><div data-key="13" class="child-of-line-12  react-code-text react-code-line-contents virtual" style="transform: translateY(260px); min-height: auto;"><div><div id="LC14" class="react-file-line html-div" data-testid="code-cell" data-line-number="14" inert="inert" style="position: relative;">    <span class="pl-k">try</span>:</div></div></div><div data-key="14" class="child-of-line-12  react-code-text react-code-line-contents virtual" style="transform: translateY(280px); min-height: auto;"><div><div id="LC15" class="react-file-line html-div" data-testid="code-cell" data-line-number="15" inert="inert" style="position: relative;">        <span class="pl-c"># Get the input values from the form</span></div></div></div><div data-key="15" class="child-of-line-12  react-code-text react-code-line-contents virtual" style="transform: translateY(300px); min-height: auto;"><div><div id="LC16" class="react-file-line html-div" data-testid="code-cell" data-line-number="16" inert="inert" style="position: relative;">        <span class="pl-s1">num_surgeries</span> <span class="pl-c1">=</span> <span class="pl-en">int</span>(<span class="pl-s1">request</span>.<span class="pl-s1">form</span>[<span class="pl-s">'num_surgeries'</span>])</div></div></div><div data-key="16" class="child-of-line-12  react-code-text react-code-line-contents virtual" style="transform: translateY(320px); min-height: auto;"><div><div id="LC17" class="react-file-line html-div" data-testid="code-cell" data-line-number="17" inert="inert" style="position: relative;">        <span class="pl-s1">num_rooms</span> <span class="pl-c1">=</span> <span class="pl-en">int</span>(<span class="pl-s1">request</span>.<span class="pl-s1">form</span>[<span class="pl-s">'num_rooms'</span>])</div></div></div><div data-key="17" class="child-of-line-12  react-code-text react-code-line-contents virtual" style="transform: translateY(340px); min-height: auto;"><div><div id="LC18" class="react-file-line html-div" data-testid="code-cell" data-line-number="18" inert="inert" style="position: relative;">        <span class="pl-s1">num_staff</span> <span class="pl-c1">=</span> <span class="pl-en">int</span>(<span class="pl-s1">request</span>.<span class="pl-s1">form</span>[<span class="pl-s">'num_staff'</span>])</div></div></div><div data-key="18" class="child-of-line-12  react-code-text react-code-line-contents virtual" style="transform: translateY(360px); min-height: auto;"><div><div id="LC19" class="react-file-line html-div" data-testid="code-cell" data-line-number="19" inert="inert" style="position: relative;">
</div></div></div><div data-key="19" class="child-of-line-12  react-code-text react-code-line-contents virtual" style="transform: translateY(380px); min-height: auto;"><div><div id="LC20" class="react-file-line html-div" data-testid="code-cell" data-line-number="20" inert="inert" style="position: relative;">        <span class="pl-c"># Get the durations of each surgery</span></div></div></div><div data-key="20" class="child-of-line-12  react-code-text react-code-line-contents virtual" style="transform: translateY(400px); min-height: auto;"><div><div id="LC21" class="react-file-line html-div" data-testid="code-cell" data-line-number="21" inert="inert" style="position: relative;">        <span class="pl-s1">durations</span> <span class="pl-c1">=</span> [<span class="pl-en">int</span>(<span class="pl-s1">request</span>.<span class="pl-s1">form</span>[<span class="pl-s">f'duration_<span class="pl-s1"><span class="pl-kos">{</span><span class="pl-s1">i</span><span class="pl-c1">+</span><span class="pl-c1">1</span><span class="pl-kos">}</span></span>'</span>]) <span class="pl-k">for</span> <span class="pl-s1">i</span> <span class="pl-c1">in</span> <span class="pl-en">range</span>(<span class="pl-s1">num_surgeries</span>)]</div></div></div><div data-key="21" class="child-of-line-12  react-code-text react-code-line-contents virtual" style="transform: translateY(420px); min-height: auto;"><div><div id="LC22" class="react-file-line html-div" data-testid="code-cell" data-line-number="22" inert="inert" style="position: relative;">
</div></div></div><div data-key="22" class="child-of-line-12  react-code-text react-code-line-contents virtual" style="transform: translateY(440px); min-height: auto;"><div><div id="LC23" class="react-file-line html-div" data-testid="code-cell" data-line-number="23" inert="inert" style="position: relative;">        <span class="pl-c"># Get staff skills for each surgery</span></div></div></div><div data-key="23" class="child-of-line-12  react-code-text react-code-line-contents virtual" style="transform: translateY(460px); min-height: auto;"><div><div id="LC24" class="react-file-line html-div" data-testid="code-cell" data-line-number="24" inert="inert" style="position: relative;">        <span class="pl-s1">staff_skills</span> <span class="pl-c1">=</span> []</div></div></div><div data-key="24" class="child-of-line-12  react-code-text react-code-line-contents virtual" style="transform: translateY(480px); min-height: auto;"><div><div id="LC25" class="react-file-line html-div" data-testid="code-cell" data-line-number="25" inert="inert" style="position: relative;">        <span class="pl-k">for</span> <span class="pl-s1">i</span> <span class="pl-c1">in</span> <span class="pl-en">range</span>(<span class="pl-s1">num_surgeries</span>):</div></div></div><div data-key="25" class="child-of-line-12  react-code-text react-code-line-contents virtual" style="transform: translateY(500px); min-height: auto;"><div><div id="LC26" class="react-file-line html-div" data-testid="code-cell" data-line-number="26" inert="inert" style="position: relative;">            <span class="pl-s1">skills</span> <span class="pl-c1">=</span> [</div></div></div><div data-key="26" class="child-of-line-12  react-code-text react-code-line-contents virtual" style="transform: translateY(520px); min-height: auto;"><div><div id="LC27" class="react-file-line html-div" data-testid="code-cell" data-line-number="27" inert="inert" style="position: relative;">                <span class="pl-en">int</span>(<span class="pl-s1">request</span>.<span class="pl-s1">form</span>.<span class="pl-en">get</span>(<span class="pl-s">f'surgery_<span class="pl-s1"><span class="pl-kos">{</span><span class="pl-s1">i</span><span class="pl-c1">+</span><span class="pl-c1">1</span><span class="pl-kos">}</span></span>_staff_<span class="pl-s1"><span class="pl-kos">{</span><span class="pl-s1">j</span><span class="pl-c1">+</span><span class="pl-c1">1</span><span class="pl-kos">}</span></span>'</span>, <span class="pl-c1">0</span>)) </div></div></div><div data-key="27" class="child-of-line-12  react-code-text react-code-line-contents virtual" style="transform: translateY(540px); min-height: auto;"><div><div id="LC28" class="react-file-line html-div" data-testid="code-cell" data-line-number="28" inert="inert" style="position: relative;">                <span class="pl-k">for</span> <span class="pl-s1">j</span> <span class="pl-c1">in</span> <span class="pl-en">range</span>(<span class="pl-c1">1</span>, <span class="pl-s1">num_staff</span> <span class="pl-c1">+</span> <span class="pl-c1">1</span>)</div></div></div><div data-key="28" class="child-of-line-12  react-code-text react-code-line-contents virtual" style="transform: translateY(560px); min-height: auto;"><div><div id="LC29" class="react-file-line html-div" data-testid="code-cell" data-line-number="29" inert="inert" style="position: relative;">            ] </div></div></div><div data-key="29" class="child-of-line-12  react-code-text react-code-line-contents virtual" style="transform: translateY(580px); min-height: auto;"><div><div id="LC30" class="react-file-line html-div" data-testid="code-cell" data-line-number="30" inert="inert" style="position: relative;">            <span class="pl-s">'''request.forms.get Retrieves the value of the form input corresponding to whether staff member j is available for surgery i+1.</span></div></div></div><div data-key="30" class="child-of-line-12  react-code-text react-code-line-contents virtual" style="transform: translateY(600px); min-height: auto;"><div><div id="LC31" class="react-file-line html-div" data-testid="code-cell" data-line-number="31" inert="inert" style="position: relative;"><span class="pl-s">Example: If i = 0 (first surgery) and j = 1 (first staff member), it looks for the input field with the name surgery_1_staff_1.</span></div></div></div><div data-key="31" class="child-of-line-12  react-code-text react-code-line-contents virtual" style="transform: translateY(620px); min-height: auto;"><div><div id="LC32" class="react-file-line html-div" data-testid="code-cell" data-line-number="32" inert="inert" style="position: relative;"><span class="pl-s">The default value is 0, meaning if the input is missing, it assumes that the staff member is unavailable for that surgery.'''</span></div></div></div><div data-key="32" class="child-of-line-12  react-code-text react-code-line-contents virtual" style="transform: translateY(640px); min-height: auto;"><div><div id="LC33" class="react-file-line html-div" data-testid="code-cell" data-line-number="33" inert="inert" style="position: relative;"><span class="pl-c">#Collect the skills (binary values: 0 or 1) of all staff members for the current surgery</span></div></div></div><div data-key="33" class="child-of-line-12  react-code-text react-code-line-contents virtual" style="transform: translateY(660px); min-height: auto;"><div><div id="LC34" class="react-file-line html-div" data-testid="code-cell" data-line-number="34" inert="inert" style="position: relative;">            <span class="pl-s1">staff_skills</span>.<span class="pl-en">append</span>(<span class="pl-s1">skills</span>)</div></div></div><div data-key="34" class="child-of-line-12  react-code-text react-code-line-contents virtual" style="transform: translateY(680px); min-height: auto;"><div><div id="LC35" class="react-file-line html-div" data-testid="code-cell" data-line-number="35" inert="inert" style="position: relative;">            <span class="pl-s">'''skills is a list Each row corresponds to a surgery.</span></div></div></div><div data-key="35" class="child-of-line-12  react-code-text react-code-line-contents virtual" style="transform: translateY(700px); min-height: auto;"><div><div id="LC36" class="react-file-line html-div" data-testid="code-cell" data-line-number="36" inert="inert" style="position: relative;"><span class="pl-s">Each element in a row is 0 or 1, indicating whether a specific staff member is available for that surgery.'''</span></div></div></div><div data-key="36" class="child-of-line-12  react-code-text react-code-line-contents virtual" style="transform: translateY(720px); min-height: auto;"><div><div id="LC37" class="react-file-line html-div" data-testid="code-cell" data-line-number="37" inert="inert" style="position: relative;">
</div></div></div><div data-key="37" class="child-of-line-12  react-code-text react-code-line-contents virtual" style="transform: translateY(740px); min-height: auto;"><div><div id="LC38" class="react-file-line html-div" data-testid="code-cell" data-line-number="38" inert="inert" style="position: relative;">        <span class="pl-c"># Generate the schedule using the genetic algorithm</span></div></div></div><div data-key="38" class="child-of-line-12  react-code-text react-code-line-contents virtual" style="transform: translateY(760px); min-height: auto;"><div><div id="LC39" class="react-file-line html-div" data-testid="code-cell" data-line-number="39" inert="inert" style="position: relative;">        <span class="pl-s1">schedule</span> <span class="pl-c1">=</span> <span class="pl-en">genetic_algorithm</span>(<span class="pl-s1">num_surgeries</span>, <span class="pl-s1">num_rooms</span>, <span class="pl-s1">num_staff</span>, <span class="pl-s1">durations</span>, <span class="pl-s1">staff_skills</span>)</div></div></div><div data-key="39" class="child-of-line-12  react-code-text react-code-line-contents virtual" style="transform: translateY(780px); min-height: auto;"><div><div id="LC40" class="react-file-line html-div" data-testid="code-cell" data-line-number="40" inert="inert" style="position: relative;">
</div></div></div><div data-key="40" class="child-of-line-12  react-code-text react-code-line-contents virtual" style="transform: translateY(800px); min-height: auto;"><div><div id="LC41" class="react-file-line html-div" data-testid="code-cell" data-line-number="41" inert="inert" style="position: relative;"> </div></div></div><div data-key="41" class="child-of-line-12  react-code-text react-code-line-contents virtual" style="transform: translateY(820px); min-height: auto;"><div><div id="LC42" class="react-file-line html-div" data-testid="code-cell" data-line-number="42" inert="inert" style="position: relative;">        <span class="pl-s">"""</span></div></div></div><div data-key="42" class="child-of-line-12  react-code-text react-code-line-contents virtual" style="transform: translateY(840px); min-height: auto;"><div><div id="LC43" class="react-file-line html-div" data-testid="code-cell" data-line-number="43" inert="inert" style="position: relative;"><span class="pl-s">            If no valid schedule is generated, display an error message.</span></div></div></div><div data-key="43" class="child-of-line-12  react-code-text react-code-line-contents virtual" style="transform: translateY(860px); min-height: auto;"><div><div id="LC44" class="react-file-line html-div" data-testid="code-cell" data-line-number="44" inert="inert" style="position: relative;"><span class="pl-s">             This may occur if inputs are inconsistent or constraints cannot be satisfied.</span></div></div></div><div data-key="44" class="child-of-line-12  react-code-text react-code-line-contents virtual" style="transform: translateY(880px); min-height: auto;"><div><div id="LC45" class="react-file-line html-div" data-testid="code-cell" data-line-number="45" inert="inert" style="position: relative;"><span class="pl-s">             """</span></div></div></div><div data-key="45" class="child-of-line-12  react-code-text react-code-line-contents virtual" style="transform: translateY(900px); min-height: auto;"><div><div id="LC46" class="react-file-line html-div" data-testid="code-cell" data-line-number="46" inert="inert" style="position: relative;">        <span class="pl-k">if</span> <span class="pl-c1">not</span> <span class="pl-s1">schedule</span>:</div></div></div><div data-key="46" class="child-of-line-12  react-code-text react-code-line-contents virtual" style="transform: translateY(920px); min-height: auto;"><div><div id="LC47" class="react-file-line html-div" data-testid="code-cell" data-line-number="47" inert="inert" style="position: relative;">            <span class="pl-s1">error</span> <span class="pl-c1">=</span> <span class="pl-s">"No valid schedule could be generated. Please check the inputs and try again."</span></div></div></div><div data-key="47" class="child-of-line-12  react-code-text react-code-line-contents virtual" style="transform: translateY(940px); min-height: auto;"><div><div id="LC48" class="react-file-line html-div" data-testid="code-cell" data-line-number="48" inert="inert" style="position: relative;">            <span class="pl-k">return</span> <span class="pl-en">render_template</span>(<span class="pl-s">'index.html'</span>, <span class="pl-s1">error</span><span class="pl-c1">=</span><span class="pl-s1">error</span>)</div></div></div><div data-key="48" class="child-of-line-12  react-code-text react-code-line-contents virtual" style="transform: translateY(960px); min-height: auto;"><div><div id="LC49" class="react-file-line html-div" data-testid="code-cell" data-line-number="49" inert="inert" style="position: relative;">        </div></div></div><div data-key="49" class="child-of-line-12  react-code-text react-code-line-contents virtual" style="transform: translateY(980px); min-height: auto;"><div><div id="LC50" class="react-file-line html-div" data-testid="code-cell" data-line-number="50" inert="inert" style="position: relative;">        <span class="pl-c"># Render the schedule on the page</span></div></div></div><div data-key="50" class="child-of-line-12  react-code-text react-code-line-contents virtual" style="transform: translateY(1000px); min-height: auto;"><div><div id="LC51" class="react-file-line html-div" data-testid="code-cell" data-line-number="51" inert="inert" style="position: relative;">        <span class="pl-k">return</span> <span class="pl-en">render_template</span>(<span class="pl-s">'index.html'</span>, <span class="pl-s1">schedule</span><span class="pl-c1">=</span><span class="pl-s1">schedule</span>)</div></div></div><div data-key="51" class="child-of-line-12  react-code-text react-code-line-contents virtual" style="transform: translateY(1020px); min-height: auto;"><div><div id="LC52" class="react-file-line html-div" data-testid="code-cell" data-line-number="52" inert="inert" style="position: relative;">
</div></div></div><div data-key="52" class="child-of-line-12  react-code-text react-code-line-contents virtual" style="transform: translateY(1040px); min-height: auto;"><div><div id="LC53" class="react-file-line html-div" data-testid="code-cell" data-line-number="53" inert="inert" style="position: relative;">    <span class="pl-k">except</span> <span class="pl-v">Exception</span> <span class="pl-k">as</span> <span class="pl-s1">e</span>:</div></div></div><div data-key="53" class="child-of-line-12  react-code-text react-code-line-contents virtual" style="transform: translateY(1060px); min-height: auto;"><div><div id="LC54" class="react-file-line html-div" data-testid="code-cell" data-line-number="54" inert="inert" style="position: relative;">        <span class="pl-c"># Handle errors gracefully and display the error message</span></div></div></div><div data-key="54" class="react-code-text react-code-line-contents virtual" style="transform: translateY(1080px); min-height: auto;"><div><div id="LC55" class="react-file-line html-div" data-testid="code-cell" data-line-number="55" inert="inert" style="position: relative;">        <span class="pl-k">return</span> <span class="pl-en">render_template</span>(<span class="pl-s">'index.html'</span>, <span class="pl-s1">error</span><span class="pl-c1">=</span><span class="pl-s">f"An error occurred: <span class="pl-s1"><span class="pl-kos">{</span><span class="pl-s1">e</span><span class="pl-kos">}</span></span>"</span>)</div></div></div><div data-key="55" class="react-code-text react-code-line-contents virtual" style="transform: translateY(1100px); min-height: auto;"><div><div id="LC56" class="react-file-line html-div" data-testid="code-cell" data-line-number="56" inert="inert" style="position: relative;">
</div></div></div><div data-key="56" class="react-code-text react-code-line-contents virtual" style="transform: translateY(1120px); min-height: auto;"><div><div id="LC57" class="react-file-line html-div" data-testid="code-cell" data-line-number="57" inert="inert" style="position: relative;"><span class="pl-c"># Genetic Algorithm for generating an optimal surgery schedule</span></div></div></div><div data-key="57" class="react-code-text react-code-line-contents virtual" style="transform: translateY(1140px); min-height: auto;"><div><div id="LC58" class="react-file-line html-div" data-testid="code-cell" data-line-number="58" inert="inert" style="position: relative;"><span class="pl-k">def</span> <span class="pl-en">genetic_algorithm</span>(<span class="pl-s1">num_surgeries</span>, <span class="pl-s1">num_rooms</span>, <span class="pl-s1">num_staff</span>, <span class="pl-s1">durations</span>, <span class="pl-s1">staff_skills</span>, <span class="pl-s1">slot_duration</span><span class="pl-c1">=</span><span class="pl-c1">40</span>, <span class="pl-s1">max_room_slots</span><span class="pl-c1">=</span><span class="pl-c1">7</span>):</div></div></div><div data-key="58" class="child-of-line-57  react-code-text react-code-line-contents virtual" style="transform: translateY(1160px); min-height: auto;"><div><div id="LC59" class="react-file-line html-div" data-testid="code-cell" data-line-number="59" inert="inert" style="position: relative;">    <span class="pl-k">import</span> <span class="pl-s1">random</span></div></div></div><div data-key="59" class="child-of-line-57  react-code-text react-code-line-contents virtual" style="transform: translateY(1180px); min-height: auto;"><div><div id="LC60" class="react-file-line html-div" data-testid="code-cell" data-line-number="60" inert="inert" style="position: relative;"><span class="pl-c"># Genetic Algorithm to generate an optimal schedule for surgeries.</span></div></div></div><div data-key="60" class="child-of-line-57  react-code-text react-code-line-contents virtual" style="transform: translateY(1200px); min-height: auto;"><div><div id="LC61" class="react-file-line html-div" data-testid="code-cell" data-line-number="61" inert="inert" style="position: relative;">    </div></div></div><div data-key="61" class="child-of-line-57  react-code-text react-code-line-contents virtual" style="transform: translateY(1220px); min-height: auto;"><div><div id="LC62" class="react-file-line html-div" data-testid="code-cell" data-line-number="62" inert="inert" style="position: relative;"><span class="pl-c">#     Parameters:</span></div></div></div><div data-key="62" class="child-of-line-57  react-code-text react-code-line-contents virtual" style="transform: translateY(1240px); min-height: auto;"><div><div id="LC63" class="react-file-line html-div" data-testid="code-cell" data-line-number="63" inert="inert" style="position: relative;"><span class="pl-c">#         num_surgeries (int): Total number of surgeries to schedule.</span></div></div></div><div data-key="63" class="child-of-line-57  react-code-text react-code-line-contents virtual" style="transform: translateY(1260px); min-height: auto;"><div><div id="LC64" class="react-file-line html-div" data-testid="code-cell" data-line-number="64" inert="inert" style="position: relative;"><span class="pl-c">#         num_rooms (int): Number of available operating rooms.</span></div></div></div><div data-key="64" class="child-of-line-57  react-code-text react-code-line-contents virtual" style="transform: translateY(1280px); min-height: auto;"><div><div id="LC65" class="react-file-line html-div" data-testid="code-cell" data-line-number="65" inert="inert" style="position: relative;"><span class="pl-c">#         num_staff (int): Total staff members available.</span></div></div></div><div data-key="65" class="child-of-line-57  react-code-text react-code-line-contents virtual" style="transform: translateY(1300px); min-height: auto;"><div><div id="LC66" class="react-file-line html-div" data-testid="code-cell" data-line-number="66" inert="inert" style="position: relative;"><span class="pl-c">#         durations (list): List of surgery durations.</span></div></div></div><div data-key="66" class="child-of-line-57  react-code-text react-code-line-contents virtual" style="transform: translateY(1320px); min-height: auto;"><div><div id="LC67" class="react-file-line html-div" data-testid="code-cell" data-line-number="67" inert="inert" style="position: relative;"><span class="pl-c">#         staff_skills (list): 2D list indicating staff eligibility for each surgery.</span></div></div></div><div data-key="67" class="child-of-line-57  react-code-text react-code-line-contents virtual" style="transform: translateY(1340px); min-height: auto;"><div><div id="LC68" class="react-file-line html-div" data-testid="code-cell" data-line-number="68" inert="inert" style="position: relative;"><span class="pl-c">#         slot_duration (int): Duration of each time slot in minutes (default: 40).</span></div></div></div><div data-key="68" class="child-of-line-57  react-code-text react-code-line-contents virtual" style="transform: translateY(1360px); min-height: auto;"><div><div id="LC69" class="react-file-line html-div" data-testid="code-cell" data-line-number="69" inert="inert" style="position: relative;"><span class="pl-c">#         max_room_slots (int): Maximum time slots available per room (default: 7).</span></div></div></div><div data-key="69" class="child-of-line-57  react-code-text react-code-line-contents virtual" style="transform: translateY(1380px); min-height: auto;"><div><div id="LC70" class="react-file-line html-div" data-testid="code-cell" data-line-number="70" inert="inert" style="position: relative;">    <span class="pl-c"># Calculate the number of slots required for each surgery</span></div></div></div><div data-key="70" class="child-of-line-57  react-code-text react-code-line-contents virtual" style="transform: translateY(1400px); min-height: auto;"><div><div id="LC71" class="react-file-line html-div" data-testid="code-cell" data-line-number="71" inert="inert" style="position: relative;">    <span class="pl-c"># (divide surgery duration by slot duration, rounding up for partial slots)</span></div></div></div><div data-key="71" class="child-of-line-57  react-code-text react-code-line-contents virtual" style="transform: translateY(1420px); min-height: auto;"><div><div id="LC72" class="react-file-line html-div" data-testid="code-cell" data-line-number="72" inert="inert" style="position: relative;">   <span class="pl-c"># Returns:</span></div></div></div><div data-key="72" class="child-of-line-57  react-code-text react-code-line-contents virtual" style="transform: translateY(1440px); min-height: auto;"><div><div id="LC73" class="react-file-line html-div" data-testid="code-cell" data-line-number="73" inert="inert" style="position: relative;"><span class="pl-c">#         list: A schedule containing surgery details or None if no valid schedule is found.</span></div></div></div><div data-key="73" class="child-of-line-57  react-code-text react-code-line-contents virtual" style="transform: translateY(1460px); min-height: auto;"><div><div id="LC74" class="react-file-line html-div" data-testid="code-cell" data-line-number="74" inert="inert" style="position: relative;">    <span class="pl-s1">slots_required</span> <span class="pl-c1">=</span> [(<span class="pl-c1">-</span>(<span class="pl-c1">-</span><span class="pl-s1">dur</span> <span class="pl-c1">//</span> <span class="pl-s1">slot_duration</span>)) <span class="pl-k">for</span> <span class="pl-s1">dur</span> <span class="pl-c1">in</span> <span class="pl-s1">durations</span>] </div></div></div><div data-key="74" class="child-of-line-57  react-code-text react-code-line-contents virtual" style="transform: translateY(1480px); min-height: auto;"><div><div id="LC75" class="react-file-line html-div" data-testid="code-cell" data-line-number="75" inert="inert" style="position: relative;">    </div></div></div><div data-key="75" class="child-of-line-57  react-code-text react-code-line-contents virtual" style="transform: translateY(1500px); min-height: auto;"><div><div id="LC76" class="react-file-line html-div" data-testid="code-cell" data-line-number="76" inert="inert" style="position: relative;">    <span class="pl-c">#to perform ceiling division using integer arithmetic</span></div></div></div><div data-key="76" class="child-of-line-57  react-code-text react-code-line-contents virtual" style="transform: translateY(1520px); min-height: auto;"><div><div id="LC77" class="react-file-line html-div" data-testid="code-cell" data-line-number="77" inert="inert" style="position: relative;">    <span class="pl-s">'''Floor division (//) truncates toward zero, while ceiling division needs to round up.</span></div></div></div><div data-key="77" class="child-of-line-57  react-code-text react-code-line-contents virtual" style="transform: translateY(1540px); min-height: auto;"><div><div id="LC78" class="react-file-line html-div" data-testid="code-cell" data-line-number="78" inert="inert" style="position: relative;"><span class="pl-s">Negating the number "reverses" the truncation direction of //, effectively performing a ceiling operation.(-(-50 // 40))  # Perform step by step</span></div></div></div><div data-key="78" class="child-of-line-57  react-code-text react-code-line-contents virtual" style="transform: translateY(1560px); min-height: auto;"><div><div id="LC79" class="react-file-line html-div" data-testid="code-cell" data-line-number="79" inert="inert" style="position: relative;"><span class="pl-s">= -((-50) // 40)</span></div></div></div><div data-key="79" class="child-of-line-57  react-code-text react-code-line-contents virtual" style="transform: translateY(1580px); min-height: auto;"><div><div id="LC80" class="react-file-line html-div" data-testid="code-cell" data-line-number="80" inert="inert" style="position: relative;"><span class="pl-s">= -(-2)  # -50 divided by 40 is -1.25, floored to -2</span></div></div></div><div data-key="80" class="child-of-line-57  react-code-text react-code-line-contents virtual" style="transform: translateY(1600px); min-height: auto;"><div><div id="LC81" class="react-file-line html-div" data-testid="code-cell" data-line-number="81" inert="inert" style="position: relative;"><span class="pl-s">= 2  '''</span></div></div></div><div data-key="81" class="child-of-line-57  react-code-text react-code-line-contents virtual" style="transform: translateY(1620px); min-height: auto;"><div><div id="LC82" class="react-file-line html-div" data-testid="code-cell" data-line-number="82" inert="inert" style="position: relative;">
</div></div></div><div data-key="82" class="child-of-line-57  react-code-text react-code-line-contents virtual" style="transform: translateY(1640px); min-height: auto;"><div><div id="LC83" class="react-file-line html-div" data-testid="code-cell" data-line-number="83" inert="inert" style="position: relative;">    <span class="pl-c"># Validate staff availability for each surgery</span></div></div></div><div data-key="83" class="child-of-line-57  react-code-text react-code-line-contents virtual" style="transform: translateY(1660px); min-height: auto;"><div><div id="LC84" class="react-file-line html-div" data-testid="code-cell" data-line-number="84" inert="inert" style="position: relative;">    <span class="pl-s1">valid_staff</span> <span class="pl-c1">=</span> []</div></div></div><div data-key="84" class="child-of-line-57  react-code-text react-code-line-contents virtual" style="transform: translateY(1680px); min-height: auto;"><div><div id="LC85" class="react-file-line html-div" data-testid="code-cell" data-line-number="85" inert="inert" style="position: relative;">    <span class="pl-k">for</span> <span class="pl-s1">i</span> <span class="pl-c1">in</span> <span class="pl-en">range</span>(<span class="pl-s1">num_surgeries</span>):</div></div></div><div data-key="85" class="child-of-line-57  react-code-text react-code-line-contents virtual" style="transform: translateY(1700px); min-height: auto;"><div><div id="LC86" class="react-file-line html-div" data-testid="code-cell" data-line-number="86" inert="inert" style="position: relative;">        <span class="pl-s">"""</span></div></div></div><div data-key="86" class="child-of-line-57  react-code-text react-code-line-contents virtual" style="transform: translateY(1720px); min-height: auto;"><div><div id="LC87" class="react-file-line html-div" data-testid="code-cell" data-line-number="87" inert="inert" style="position: relative;"><span class="pl-s">       Collect a list of staff members eligible for each surgery.</span></div></div></div><div data-key="87" class="child-of-line-57  react-code-text react-code-line-contents virtual" style="transform: translateY(1740px); min-height: auto;"><div><div id="LC88" class="react-file-line html-div" data-testid="code-cell" data-line-number="88" inert="inert" style="position: relative;"><span class="pl-s">         If no staff is available for a surgery, return None to indicate an invalid schedule.</span></div></div></div><div data-key="88" class="child-of-line-57  react-code-text react-code-line-contents virtual" style="transform: translateY(1760px); min-height: auto;"><div><div id="LC89" class="react-file-line html-div" data-testid="code-cell" data-line-number="89" inert="inert" style="position: relative;"><span class="pl-s">         """</span></div></div></div><div data-key="89" class="child-of-line-57  react-code-text react-code-line-contents virtual" style="transform: translateY(1780px); min-height: auto;"><div><div id="LC90" class="react-file-line html-div" data-testid="code-cell" data-line-number="90" inert="inert" style="position: relative;">        <span class="pl-s1">staff_for_surgery</span> <span class="pl-c1">=</span> [<span class="pl-s1">s</span> <span class="pl-c1">+</span> <span class="pl-c1">1</span> <span class="pl-k">for</span> <span class="pl-s1">s</span>, <span class="pl-s1">can_do</span> <span class="pl-c1">in</span> <span class="pl-en">enumerate</span>(<span class="pl-s1">staff_skills</span>[<span class="pl-s1">i</span>]) ]</div></div></div><div data-key="90" class="child-of-line-57  react-code-text react-code-line-contents virtual" style="transform: translateY(1800px); min-height: auto;"><div><div id="LC91" class="react-file-line html-div" data-testid="code-cell" data-line-number="91" inert="inert" style="position: relative;">        <span class="pl-k">if</span> <span class="pl-c1">not</span> <span class="pl-s1">staff_for_surgery</span>:</div></div></div><div data-key="91" class="child-of-line-57  react-code-text react-code-line-contents virtual" style="transform: translateY(1820px); min-height: auto;"><div><div id="LC92" class="react-file-line html-div" data-testid="code-cell" data-line-number="92" inert="inert" style="position: relative;">            <span class="pl-k">return</span> <span class="pl-c1">None</span>  <span class="pl-c"># If no staff is available for a surgery, return an invalid schedule</span></div></div></div><div data-key="92" class="child-of-line-57  react-code-text react-code-line-contents virtual" style="transform: translateY(1840px); min-height: auto;"><div><div id="LC93" class="react-file-line html-div" data-testid="code-cell" data-line-number="93" inert="inert" style="position: relative;">        <span class="pl-s1">valid_staff</span>.<span class="pl-en">append</span>(<span class="pl-s1">staff_for_surgery</span>)</div></div></div><div data-key="93" class="child-of-line-57  react-code-text react-code-line-contents virtual" style="transform: translateY(1860px); min-height: auto;"><div><div id="LC94" class="react-file-line html-div" data-testid="code-cell" data-line-number="94" inert="inert" style="position: relative;">
</div></div></div><div data-key="94" class="child-of-line-57  react-code-text react-code-line-contents virtual" style="transform: translateY(1880px); min-height: auto;"><div><div id="LC95" class="react-file-line html-div" data-testid="code-cell" data-line-number="95" inert="inert" style="position: relative;">    <span class="pl-c"># Step 1: Initialize the population with random schedules</span></div></div></div><div data-key="95" class="child-of-line-57  react-code-text react-code-line-contents virtual" style="transform: translateY(1900px); min-height: auto;"><div><div id="LC96" class="react-file-line html-div" data-testid="code-cell" data-line-number="96" inert="inert" style="position: relative;">    <span class="pl-s1">population</span> <span class="pl-c1">=</span> []</div></div></div><div data-key="96" class="child-of-line-57  react-code-text react-code-line-contents virtual" style="transform: translateY(1920px); min-height: auto;"><div><div id="LC97" class="react-file-line html-div" data-testid="code-cell" data-line-number="97" inert="inert" style="position: relative;">    <span class="pl-k">for</span> <span class="pl-s1">_</span> <span class="pl-c1">in</span> <span class="pl-en">range</span>(<span class="pl-c1">50</span>):  <span class="pl-c"># Population size of 50</span></div></div></div><div data-key="97" class="child-of-line-57  react-code-text react-code-line-contents virtual" style="transform: translateY(1940px); min-height: auto;"><div><div id="LC98" class="react-file-line html-div" data-testid="code-cell" data-line-number="98" inert="inert" style="position: relative;">        <span class="pl-s">"""</span></div></div></div><div data-key="98" class="child-of-line-57  react-code-text react-code-line-contents virtual" style="transform: translateY(1960px); min-height: auto;"><div><div id="LC99" class="react-file-line html-div" data-testid="code-cell" data-line-number="99" inert="inert" style="position: relative;"><span class="pl-s">       Create a random schedule for each individual in the population.</span></div></div></div><div data-key="99" class="child-of-line-57  react-code-text react-code-line-contents virtual" style="transform: translateY(1980px); min-height: auto;"><div><div id="LC100" class="react-file-line html-div" data-testid="code-cell" data-line-number="100" inert="inert" style="position: relative;"><span class="pl-s">         Assign surgeries to random rooms, time slots, and eligible staff members.</span></div></div></div><div data-key="100" class="child-of-line-57  react-code-text react-code-line-contents virtual" style="transform: translateY(2000px); min-height: auto;"><div><div id="LC101" class="react-file-line html-div" data-testid="code-cell" data-line-number="101" inert="inert" style="position: relative;"><span class="pl-s">         """</span></div></div></div><div data-key="101" class="child-of-line-57  react-code-text react-code-line-contents virtual" style="transform: translateY(2020px); min-height: auto;"><div><div id="LC102" class="react-file-line html-div" data-testid="code-cell" data-line-number="102" inert="inert" style="position: relative;">        <span class="pl-s1">individual</span> <span class="pl-c1">=</span> []</div></div></div><div data-key="102" class="child-of-line-57  react-code-text react-code-line-contents virtual" style="transform: translateY(2040px); min-height: auto;"><div><div id="LC103" class="react-file-line html-div" data-testid="code-cell" data-line-number="103" inert="inert" style="position: relative;">        <span class="pl-k">for</span> <span class="pl-s1">i</span> <span class="pl-c1">in</span> <span class="pl-en">range</span>(<span class="pl-s1">num_surgeries</span>):</div></div></div><div data-key="103" class="child-of-line-57  react-code-text react-code-line-contents virtual" style="transform: translateY(2060px); min-height: auto;"><div><div id="LC104" class="react-file-line html-div" data-testid="code-cell" data-line-number="104" inert="inert" style="position: relative;">            <span class="pl-s1">room</span> <span class="pl-c1">=</span> <span class="pl-s1">random</span>.<span class="pl-en">randint</span>(<span class="pl-c1">1</span>, <span class="pl-s1">num_rooms</span>)  <span class="pl-c"># Assign a random room</span></div></div></div><div data-key="104" class="child-of-line-57  react-code-text react-code-line-contents virtual" style="transform: translateY(2080px); min-height: auto;"><div><div id="LC105" class="react-file-line html-div" data-testid="code-cell" data-line-number="105" inert="inert" style="position: relative;">            <span class="pl-s1">start_slot</span> <span class="pl-c1">=</span> <span class="pl-s1">random</span>.<span class="pl-en">randint</span>(<span class="pl-c1">1</span>, <span class="pl-s1">max_room_slots</span> <span class="pl-c1">-</span> <span class="pl-s1">slots_required</span>[<span class="pl-s1">i</span>] <span class="pl-c1">+</span> <span class="pl-c1">1</span>)  <span class="pl-c"># Assign a random starting slot</span></div></div></div><div data-key="105" class="child-of-line-57  react-code-text react-code-line-contents virtual" style="transform: translateY(2100px); min-height: auto;"><div><div id="LC106" class="react-file-line html-div" data-testid="code-cell" data-line-number="106" inert="inert" style="position: relative;">            <span class="pl-s1">assigned_staff</span> <span class="pl-c1">=</span> <span class="pl-s1">random</span>.<span class="pl-en">sample</span>(<span class="pl-s1">valid_staff</span>[<span class="pl-s1">i</span>], <span class="pl-s1">k</span><span class="pl-c1">=</span><span class="pl-c1">1</span>)  <span class="pl-c"># Randomly assign at least one valid staff member</span></div></div></div><div data-key="106" class="child-of-line-57  react-code-text react-code-line-contents virtual" style="transform: translateY(2120px); min-height: auto;"><div><div id="LC107" class="react-file-line html-div" data-testid="code-cell" data-line-number="107" inert="inert" style="position: relative;">            <span class="pl-s1">individual</span>.<span class="pl-en">append</span>({</div></div></div><div data-key="107" class="child-of-line-57  react-code-text react-code-line-contents virtual" style="transform: translateY(2140px); min-height: auto;"><div><div id="LC108" class="react-file-line html-div" data-testid="code-cell" data-line-number="108" inert="inert" style="position: relative;">                <span class="pl-s">"surgery"</span>: <span class="pl-s1">i</span> <span class="pl-c1">+</span> <span class="pl-c1">1</span>, </div></div></div><div data-key="108" class="child-of-line-57  react-code-text react-code-line-contents virtual" style="transform: translateY(2160px); min-height: auto;"><div><div id="LC109" class="react-file-line html-div" data-testid="code-cell" data-line-number="109" inert="inert" style="position: relative;">                <span class="pl-s">"room"</span>: <span class="pl-s1">room</span>,  <span class="pl-c"># Assigned room</span></div></div></div><div data-key="109" class="child-of-line-57  react-code-text react-code-line-contents virtual" style="transform: translateY(2180px); min-height: auto;"><div><div id="LC110" class="react-file-line html-div" data-testid="code-cell" data-line-number="110" inert="inert" style="position: relative;">                <span class="pl-s">"start_slot"</span>: <span class="pl-s1">start_slot</span>,  <span class="pl-c"># Starting time slot</span></div></div></div><div data-key="110" class="child-of-line-57  react-code-text react-code-line-contents virtual" style="transform: translateY(2200px); min-height: auto;"><div><div id="LC111" class="react-file-line html-div" data-testid="code-cell" data-line-number="111" inert="inert" style="position: relative;">                <span class="pl-s">"end_slot"</span>: <span class="pl-s1">start_slot</span> <span class="pl-c1">+</span> <span class="pl-s1">slots_required</span>[<span class="pl-s1">i</span>] <span class="pl-c1">-</span> <span class="pl-c1">1</span>,  <span class="pl-c"># Ending time slot</span></div></div></div><div data-key="111" class="child-of-line-57  react-code-text react-code-line-contents virtual" style="transform: translateY(2220px); min-height: auto;"><div><div id="LC112" class="react-file-line html-div" data-testid="code-cell" data-line-number="112" inert="inert" style="position: relative;">                <span class="pl-s">"staff"</span>: <span class="pl-s1">assigned_staff</span>  <span class="pl-c"># Assigned staff members</span></div></div></div><div data-key="112" class="child-of-line-57  react-code-text react-code-line-contents virtual" style="transform: translateY(2240px); min-height: auto;"><div><div id="LC113" class="react-file-line html-div" data-testid="code-cell" data-line-number="113" inert="inert" style="position: relative;">            })</div></div></div><div data-key="113" class="child-of-line-57  react-code-text react-code-line-contents virtual" style="transform: translateY(2260px); min-height: auto;"><div><div id="LC114" class="react-file-line html-div" data-testid="code-cell" data-line-number="114" inert="inert" style="position: relative;">        <span class="pl-s1">population</span>.<span class="pl-en">append</span>(<span class="pl-s1">individual</span>)</div></div></div><div data-key="114" class="child-of-line-57  react-code-text react-code-line-contents virtual" style="transform: translateY(2280px); min-height: auto;"><div><div id="LC115" class="react-file-line html-div" data-testid="code-cell" data-line-number="115" inert="inert" style="position: relative;">
</div></div></div><div data-key="115" class="child-of-line-57  react-code-text react-code-line-contents virtual" style="transform: translateY(2300px); min-height: auto;"><div><div id="LC116" class="react-file-line html-div" data-testid="code-cell" data-line-number="116" inert="inert" style="position: relative;">    <span class="pl-c"># Fitness Function: Evaluate the quality of a schedule</span></div></div></div><div data-key="116" class="child-of-line-57  react-code-text react-code-line-contents virtual" style="transform: translateY(2320px); min-height: auto;"><div><div id="LC117" class="react-file-line html-div" data-testid="code-cell" data-line-number="117" inert="inert" style="position: relative;">    <span class="pl-k">def</span> <span class="pl-en">fitness</span>(<span class="pl-s1">individual</span>):</div></div></div><div data-key="117" class="child-of-line-57 child-of-line-116  react-code-text react-code-line-contents virtual" style="transform: translateY(2340px); min-height: auto;"><div><div id="LC118" class="react-file-line html-div" data-testid="code-cell" data-line-number="118" inert="inert" style="position: relative;">
</div></div></div><div data-key="133" class="child-of-line-57 child-of-line-116  react-code-text react-code-line-contents virtual" style="transform: translateY(2660px); min-height: auto;"><div><div id="LC134" class="react-file-line html-div" data-testid="code-cell" data-line-number="134" inert="inert" style="position: relative;">            <span class="pl-s1">end</span> <span class="pl-c1">=</span> <span class="pl-s1">surgery</span>[<span class="pl-s">"end_slot"</span>]</div></div></div><div data-key="134" class="child-of-line-57 child-of-line-116  react-code-text react-code-line-contents virtual" style="transform: translateY(2680px); min-height: auto;"><div><div id="LC135" class="react-file-line html-div" data-testid="code-cell" data-line-number="135" inert="inert" style="position: relative;">
</div></div></div><div data-key="135" class="child-of-line-57 child-of-line-116  react-code-text react-code-line-contents virtual" style="transform: translateY(2700px); min-height: auto;"><div><div id="LC136" class="react-file-line html-div" data-testid="code-cell" data-line-number="136" inert="inert" style="position: relative;">            <span class="pl-c"># Penalize overlapping surgeries in the same room</span></div></div></div><div data-key="136" class="child-of-line-57 child-of-line-116  react-code-text react-code-line-contents virtual" style="transform: translateY(2720px); min-height: auto;"><div><div id="LC137" class="react-file-line html-div" data-testid="code-cell" data-line-number="137" inert="inert" style="position: relative;">            <span class="pl-k">for</span> <span class="pl-s1">booked</span> <span class="pl-c1">in</span> <span class="pl-s1">room_schedule</span>[<span class="pl-s1">room</span>]:</div></div></div><div data-key="137" class="child-of-line-57 child-of-line-116  react-code-text react-code-line-contents virtual" style="transform: translateY(2740px); min-height: auto;"><div><div id="LC138" class="react-file-line html-div" data-testid="code-cell" data-line-number="138" inert="inert" style="position: relative;">                <span class="pl-k">if</span> <span class="pl-c1">not</span> (<span class="pl-s1">end</span> <span class="pl-c1">&lt;</span> <span class="pl-s1">booked</span>[<span class="pl-c1">0</span>] <span class="pl-c1">or</span> <span class="pl-s1">start</span> <span class="pl-c1">&gt;</span> <span class="pl-s1">booked</span>[<span class="pl-c1">1</span>]):  <span class="pl-c"># Overlap detected</span></div></div></div><div data-key="138" class="child-of-line-57 child-of-line-116  react-code-text react-code-line-contents virtual" style="transform: translateY(2760px); min-height: auto;"><div><div id="LC139" class="react-file-line html-div" data-testid="code-cell" data-line-number="139" inert="inert" style="position: relative;">                    <span class="pl-s1">score</span> <span class="pl-c1">-=</span> <span class="pl-c1">10</span></div></div></div><div data-key="139" class="child-of-line-57 child-of-line-116  react-code-text react-code-line-contents virtual" style="transform: translateY(2780px); min-height: auto;"><div><div id="LC140" class="react-file-line html-div" data-testid="code-cell" data-line-number="140" inert="inert" style="position: relative;">
</div></div></div><div data-key="140" class="child-of-line-57 child-of-line-116  react-code-text react-code-line-contents virtual" style="transform: translateY(2800px); min-height: auto;"><div><div id="LC141" class="react-file-line html-div" data-testid="code-cell" data-line-number="141" inert="inert" style="position: relative;">            <span class="pl-c"># Penalize invalid staff assignments</span></div></div></div><div data-key="141" class="child-of-line-57 child-of-line-116  react-code-text react-code-line-contents virtual" style="transform: translateY(2820px); min-height: auto;"><div><div id="LC142" class="react-file-line html-div" data-testid="code-cell" data-line-number="142" inert="inert" style="position: relative;">            <span class="pl-k">for</span> <span class="pl-s1">staff</span> <span class="pl-c1">in</span> <span class="pl-s1">surgery</span>[<span class="pl-s">"staff"</span>]:</div></div></div><div data-key="142" class="child-of-line-57 child-of-line-116  react-code-text react-code-line-contents virtual" style="transform: translateY(2840px); min-height: auto;"><div><div id="LC143" class="react-file-line html-div" data-testid="code-cell" data-line-number="143" inert="inert" style="position: relative;">                <span class="pl-k">if</span> <span class="pl-s1">staff</span> <span class="pl-c1">not</span> <span class="pl-c1">in</span> <span class="pl-s1">valid_staff</span>[<span class="pl-s1">surgery</span>[<span class="pl-s">"surgery"</span>] <span class="pl-c1">-</span> <span class="pl-c1">1</span>]:</div></div></div><div data-key="143" class="child-of-line-57 child-of-line-116  react-code-text react-code-line-contents virtual" style="transform: translateY(2860px); min-height: auto;"><div><div id="LC144" class="react-file-line html-div" data-testid="code-cell" data-line-number="144" inert="inert" style="position: relative;">                    <span class="pl-s1">score</span> <span class="pl-c1">-=</span> <span class="pl-c1">1</span>   <span class="pl-c">#changed from 15</span></div></div></div><div data-key="144" class="child-of-line-57 child-of-line-116  react-code-text react-code-line-contents virtual" style="transform: translateY(2880px); min-height: auto;"><div><div id="LC145" class="react-file-line html-div" data-testid="code-cell" data-line-number="145" inert="inert" style="position: relative;">
</div></div></div><div data-key="145" class="child-of-line-57 child-of-line-116  react-code-text react-code-line-contents virtual" style="transform: translateY(2900px); min-height: auto;"><div><div id="LC146" class="react-file-line html-div" data-testid="code-cell" data-line-number="146" inert="inert" style="position: relative;">            <span class="pl-c"># Update the room's schedule</span></div></div></div><div data-key="146" class="child-of-line-57 child-of-line-116  react-code-text react-code-line-contents virtual" style="transform: translateY(2920px); min-height: auto;"><div><div id="LC147" class="react-file-line html-div" data-testid="code-cell" data-line-number="147" inert="inert" style="position: relative;">            <span class="pl-s1">room_schedule</span>[<span class="pl-s1">room</span>].<span class="pl-en">append</span>((<span class="pl-s1">start</span>, <span class="pl-s1">end</span>))</div></div></div><div data-key="147" class="child-of-line-57 child-of-line-116  react-code-text react-code-line-contents virtual" style="transform: translateY(2940px); min-height: auto;"><div><div id="LC148" class="react-file-line html-div" data-testid="code-cell" data-line-number="148" inert="inert" style="position: relative;">            <span class="pl-s1">score</span> <span class="pl-c1">+=</span> <span class="pl-c1">1</span>  <span class="pl-c"># Reward valid room and staff assignments changed from 5 to 1</span></div></div></div><div data-key="148" class="child-of-line-57 child-of-line-116  react-code-text react-code-line-contents virtual" style="transform: translateY(2960px); min-height: auto;"><div><div id="LC149" class="react-file-line html-div" data-testid="code-cell" data-line-number="149" inert="inert" style="position: relative;">
</div></div></div><div data-key="149" class="child-of-line-57  react-code-text react-code-line-contents virtual" style="transform: translateY(2980px); min-height: auto;"><div><div id="LC150" class="react-file-line html-div" data-testid="code-cell" data-line-number="150" inert="inert" style="position: relative;">        <span class="pl-k">return</span> <span class="pl-s1">score</span></div></div></div><div data-key="150" class="child-of-line-57  react-code-text react-code-line-contents virtual" style="transform: translateY(3000px); min-height: auto;"><div><div id="LC151" class="react-file-line html-div" data-testid="code-cell" data-line-number="151" inert="inert" style="position: relative;">
</div></div></div><div data-key="151" class="child-of-line-57  react-code-text react-code-line-contents virtual" style="transform: translateY(3020px); min-height: auto;"><div><div id="LC152" class="react-file-line html-div" data-testid="code-cell" data-line-number="152" inert="inert" style="position: relative;">    <span class="pl-c"># Evolution Function: Create the next generation of schedules</span></div></div></div><div data-key="152" class="child-of-line-57  react-code-text react-code-line-contents virtual" style="transform: translateY(3040px); min-height: auto;"><div><div id="LC153" class="react-file-line html-div" data-testid="code-cell" data-line-number="153" inert="inert" style="position: relative;">    <span class="pl-k">def</span> <span class="pl-en">evolve</span>(<span class="pl-s1">population</span>):</div></div></div><div data-key="153" class="child-of-line-57 child-of-line-152  react-code-text react-code-line-contents virtual" style="transform: translateY(3060px); min-height: auto;"><div><div id="LC154" class="react-file-line html-div" data-testid="code-cell" data-line-number="154" inert="inert" style="position: relative;">        </div></div></div><div data-key="154" class="child-of-line-57 child-of-line-152  react-code-text react-code-line-contents virtual" style="transform: translateY(3080px); min-height: auto;"><div><div id="LC155" class="react-file-line html-div" data-testid="code-cell" data-line-number="155" inert="inert" style="position: relative;">        <span class="pl-c"># Sort the population by fitness (higher is better)</span></div></div></div><div data-key="155" class="child-of-line-57 child-of-line-152  react-code-text react-code-line-contents virtual" style="transform: translateY(3100px); min-height: auto;"><div><div id="LC156" class="react-file-line html-div" data-testid="code-cell" data-line-number="156" inert="inert" style="position: relative;">        <span class="pl-s1">population</span>.<span class="pl-en">sort</span>(<span class="pl-s1">key</span><span class="pl-c1">=</span><span class="pl-k">lambda</span> <span class="pl-s1">x</span>: <span class="pl-en">fitness</span>(<span class="pl-s1">x</span>), <span class="pl-s1">reverse</span><span class="pl-c1">=</span><span class="pl-c1">True</span>)</div></div></div><div data-key="156" class="child-of-line-57 child-of-line-152  react-code-text react-code-line-contents virtual" style="transform: translateY(3120px); min-height: auto;"><div><div id="LC157" class="react-file-line html-div" data-testid="code-cell" data-line-number="157" inert="inert" style="position: relative;">
</div></div></div><div data-key="157" class="child-of-line-57 child-of-line-152  react-code-text react-code-line-contents virtual" style="transform: translateY(3140px); min-height: auto;"><div><div id="LC158" class="react-file-line html-div" data-testid="code-cell" data-line-number="158" inert="inert" style="position: relative;">        <span class="pl-c"># Select the top 10 schedules as parents for the next generation</span></div></div></div><div data-key="158" class="child-of-line-57 child-of-line-152  react-code-text react-code-line-contents virtual" style="transform: translateY(3160px); min-height: auto;"><div><div id="LC159" class="react-file-line html-div" data-testid="code-cell" data-line-number="159" inert="inert" style="position: relative;">        <span class="pl-s1">new_population</span> <span class="pl-c1">=</span> <span class="pl-s1">population</span>[:<span class="pl-c1">10</span>]</div></div></div><div data-key="159" class="child-of-line-57 child-of-line-152  react-code-text react-code-line-contents virtual" style="transform: translateY(3180px); min-height: auto;"><div><div id="LC160" class="react-file-line html-div" data-testid="code-cell" data-line-number="160" inert="inert" style="position: relative;">
</div></div></div><div data-key="160" class="child-of-line-57 child-of-line-152  react-code-text react-code-line-contents virtual" style="transform: translateY(3200px); min-height: auto;"><div><div id="LC161" class="react-file-line html-div" data-testid="code-cell" data-line-number="161" inert="inert" style="position: relative;">        <span class="pl-c"># Generate new individuals by crossover and mutation until the population is full</span></div></div></div><div data-key="161" class="child-of-line-57 child-of-line-152  react-code-text react-code-line-contents virtual" style="transform: translateY(3220px); min-height: auto;"><div><div id="LC162" class="react-file-line html-div" data-testid="code-cell" data-line-number="162" inert="inert" style="position: relative;">        <span class="pl-k">while</span> <span class="pl-en">len</span>(<span class="pl-s1">new_population</span>) <span class="pl-c1">&lt;</span> <span class="pl-c1">50</span>:</div></div></div><div data-key="162" class="child-of-line-57 child-of-line-152  react-code-text react-code-line-contents virtual" style="transform: translateY(3240px); min-height: auto;"><div><div id="LC163" class="react-file-line html-div" data-testid="code-cell" data-line-number="163" inert="inert" style="position: relative;">            <span class="pl-c"># Select two parents from the top 10 fittest schedules</span></div></div></div><div data-key="163" class="child-of-line-57 child-of-line-152  react-code-text react-code-line-contents virtual" style="transform: translateY(3260px); min-height: auto;"><div><div id="LC164" class="react-file-line html-div" data-testid="code-cell" data-line-number="164" inert="inert" style="position: relative;">            <span class="pl-s1">p1</span>, <span class="pl-s1">p2</span> <span class="pl-c1">=</span> <span class="pl-s1">random</span>.<span class="pl-en">sample</span>(<span class="pl-s1">population</span>[:<span class="pl-c1">10</span>], <span class="pl-c1">2</span>)</div></div></div><div data-key="164" class="child-of-line-57 child-of-line-152  react-code-text react-code-line-contents virtual" style="transform: translateY(3280px); min-height: auto;"><div><div id="LC165" class="react-file-line html-div" data-testid="code-cell" data-line-number="165" inert="inert" style="position: relative;">
</div></div></div><div data-key="165" class="child-of-line-57 child-of-line-152  react-code-text react-code-line-contents virtual" style="transform: translateY(3300px); min-height: auto;"><div><div id="LC166" class="react-file-line html-div" data-testid="code-cell" data-line-number="166" inert="inert" style="position: relative;">            <span class="pl-c"># Perform crossover by combining parts of the parents</span></div></div></div><div data-key="166" class="child-of-line-57 child-of-line-152  react-code-text react-code-line-contents virtual" style="transform: translateY(3320px); min-height: auto;"><div><div id="LC167" class="react-file-line html-div" data-testid="code-cell" data-line-number="167" inert="inert" style="position: relative;">            <span class="pl-s1">crossover_point</span> <span class="pl-c1">=</span> <span class="pl-s1">random</span>.<span class="pl-en">randint</span>(<span class="pl-c1">0</span>, <span class="pl-s1">num_surgeries</span> <span class="pl-c1">-</span> <span class="pl-c1">1</span>)</div></div></div><div data-key="167" class="child-of-line-57 child-of-line-152  react-code-text react-code-line-contents virtual" style="transform: translateY(3340px); min-height: auto;"><div><div id="LC168" class="react-file-line html-div" data-testid="code-cell" data-line-number="168" inert="inert" style="position: relative;">            <span class="pl-s1">child</span> <span class="pl-c1">=</span> <span class="pl-s1">p1</span>[:<span class="pl-s1">crossover_point</span>] <span class="pl-c1">+</span> <span class="pl-s1">p2</span>[<span class="pl-s1">crossover_point</span>:]</div></div></div><div data-key="168" class="child-of-line-57 child-of-line-152  react-code-text react-code-line-contents virtual" style="transform: translateY(3360px); min-height: auto;"><div><div id="LC169" class="react-file-line html-div" data-testid="code-cell" data-line-number="169" inert="inert" style="position: relative;">
</div></div></div><div data-key="169" class="child-of-line-57 child-of-line-152  react-code-text react-code-line-contents virtual" style="transform: translateY(3380px); min-height: auto;"><div><div id="LC170" class="react-file-line html-div" data-testid="code-cell" data-line-number="170" inert="inert" style="position: relative;">            <span class="pl-c"># Mutation: Randomly adjust room or starting slot for some surgeries</span></div></div></div><div data-key="170" class="child-of-line-57 child-of-line-152  react-code-text react-code-line-contents virtual" style="transform: translateY(3400px); min-height: auto;"><div><div id="LC171" class="react-file-line html-div" data-testid="code-cell" data-line-number="171" inert="inert" style="position: relative;">            <span class="pl-k">if</span> <span class="pl-s1">random</span>.<span class="pl-en">random</span>() <span class="pl-c1">&lt;</span> <span class="pl-c1">0.01</span>:  <span class="pl-c"># 1% chance of mutation</span></div></div></div><div data-key="171" class="child-of-line-57 child-of-line-152  react-code-text react-code-line-contents virtual" style="transform: translateY(3420px); min-height: auto;"><div><div id="LC172" class="react-file-line html-div" data-testid="code-cell" data-line-number="172" inert="inert" style="position: relative;">                <span class="pl-s1">idx</span> <span class="pl-c1">=</span> <span class="pl-s1">random</span>.<span class="pl-en">randint</span>(<span class="pl-c1">0</span>, <span class="pl-s1">num_surgeries</span> <span class="pl-c1">-</span> <span class="pl-c1">1</span>)  <span class="pl-c"># Select a random surgery to mutate</span></div></div></div><div data-key="172" class="child-of-line-57 child-of-line-152  react-code-text react-code-line-contents virtual" style="transform: translateY(3440px); min-height: auto;"><div><div id="LC173" class="react-file-line html-div" data-testid="code-cell" data-line-number="173" inert="inert" style="position: relative;">                <span class="pl-s1">child</span>[<span class="pl-s1">idx</span>][<span class="pl-s">"room"</span>] <span class="pl-c1">=</span> <span class="pl-s1">random</span>.<span class="pl-en">randint</span>(<span class="pl-c1">1</span>, <span class="pl-s1">num_rooms</span>)  <span class="pl-c"># Assign a new random room</span></div></div></div><div data-key="173" class="child-of-line-57 child-of-line-152  react-code-text react-code-line-contents virtual" style="transform: translateY(3460px); min-height: auto;"><div><div id="LC174" class="react-file-line html-div" data-testid="code-cell" data-line-number="174" inert="inert" style="position: relative;">                <span class="pl-s1">child</span>[<span class="pl-s1">idx</span>][<span class="pl-s">"start_slot"</span>] <span class="pl-c1">=</span> <span class="pl-s1">random</span>.<span class="pl-en">randint</span>(<span class="pl-c1">1</span>, <span class="pl-s1">max_room_slots</span> <span class="pl-c1">-</span> <span class="pl-s1">slots_required</span>[<span class="pl-s1">idx</span>] <span class="pl-c1">+</span> <span class="pl-c1">1</span>)  <span class="pl-c"># Assign a new random start slot</span></div></div></div><div data-key="174" class="child-of-line-57 child-of-line-152  react-code-text react-code-line-contents virtual" style="transform: translateY(3480px); min-height: auto;"><div><div id="LC175" class="react-file-line html-div" data-testid="code-cell" data-line-number="175" inert="inert" style="position: relative;">
</div></div></div><div data-key="175" class="child-of-line-57 child-of-line-152  react-code-text react-code-line-contents virtual" style="transform: translateY(3500px); min-height: auto;"><div><div id="LC176" class="react-file-line html-div" data-testid="code-cell" data-line-number="176" inert="inert" style="position: relative;">            <span class="pl-c"># Add the mutated child to the new population</span></div></div></div><div data-key="176" class="child-of-line-57 child-of-line-152  react-code-text react-code-line-contents virtual" style="transform: translateY(3520px); min-height: auto;"><div><div id="LC177" class="react-file-line html-div" data-testid="code-cell" data-line-number="177" inert="inert" style="position: relative;">            <span class="pl-s1">new_population</span>.<span class="pl-en">append</span>(<span class="pl-s1">child</span>)</div></div></div><div data-key="177" class="child-of-line-57 child-of-line-152  react-code-text react-code-line-contents virtual" style="transform: translateY(3540px); min-height: auto;"><div><div id="LC178" class="react-file-line html-div" data-testid="code-cell" data-line-number="178" inert="inert" style="position: relative;">
</div></div></div><div data-key="178" class="child-of-line-57  react-code-text react-code-line-contents virtual" style="transform: translateY(3560px); min-height: auto;"><div><div id="LC179" class="react-file-line html-div" data-testid="code-cell" data-line-number="179" inert="inert" style="position: relative;">        <span class="pl-k">return</span> <span class="pl-s1">new_population</span></div></div></div><div data-key="179" class="child-of-line-57  react-code-text react-code-line-contents virtual" style="transform: translateY(3580px); min-height: auto;"><div><div id="LC180" class="react-file-line html-div" data-testid="code-cell" data-line-number="180" inert="inert" style="position: relative;">
</div></div></div><div data-key="180" class="child-of-line-57  react-code-text react-code-line-contents virtual" style="transform: translateY(3600px); min-height: auto;"><div><div id="LC181" class="react-file-line html-div" data-testid="code-cell" data-line-number="181" inert="inert" style="position: relative;">    <span class="pl-c"># Step 2: Run the genetic algorithm for a fixed number of generations</span></div></div></div><div data-key="181" class="child-of-line-57  react-code-text react-code-line-contents virtual" style="transform: translateY(3620px); min-height: auto;"><div><div id="LC182" class="react-file-line html-div" data-testid="code-cell" data-line-number="182" inert="inert" style="position: relative;">    <span class="pl-k">for</span> <span class="pl-s1">_</span> <span class="pl-c1">in</span> <span class="pl-en">range</span>(<span class="pl-c1">50</span>):  <span class="pl-c"># Run for 50 generations</span></div></div></div><div data-key="182" class="child-of-line-57  react-code-text react-code-line-contents virtual" style="transform: translateY(3640px); min-height: auto;"><div><div id="LC183" class="react-file-line html-div" data-testid="code-cell" data-line-number="183" inert="inert" style="position: relative;">        <span class="pl-s1">population</span> <span class="pl-c1">=</span> <span class="pl-en">evolve</span>(<span class="pl-s1">population</span>)  <span class="pl-c"># Evolve the population</span></div></div></div><div data-key="183" class="child-of-line-57  react-code-text react-code-line-contents virtual" style="transform: translateY(3660px); min-height: auto;"><div><div id="LC184" class="react-file-line html-div" data-testid="code-cell" data-line-number="184" inert="inert" style="position: relative;">
</div></div></div><div data-key="184" class="child-of-line-57  react-code-text react-code-line-contents virtual" style="transform: translateY(3680px); min-height: auto;"><div><div id="LC185" class="react-file-line html-div" data-testid="code-cell" data-line-number="185" inert="inert" style="position: relative;">    <span class="pl-c"># Step 3: Select the best schedule from the final generation</span></div></div></div><div data-key="185" class="child-of-line-57  react-code-text react-code-line-contents virtual" style="transform: translateY(3700px); min-height: auto;"><div><div id="LC186" class="react-file-line html-div" data-testid="code-cell" data-line-number="186" inert="inert" style="position: relative;">    <span class="pl-s1">best_schedule</span> <span class="pl-c1">=</span> <span class="pl-en">max</span>(<span class="pl-s1">population</span>, <span class="pl-s1">key</span><span class="pl-c1">=</span><span class="pl-k">lambda</span> <span class="pl-s1">x</span>: <span class="pl-en">fitness</span>(<span class="pl-s1">x</span>))</div></div></div><div data-key="186" class="child-of-line-57  react-code-text react-code-line-contents virtual" style="transform: translateY(3720px); min-height: auto;"><div><div id="LC187" class="react-file-line html-div" data-testid="code-cell" data-line-number="187" inert="inert" style="position: relative;">
</div></div></div><div data-key="187" class="child-of-line-57  react-code-text react-code-line-contents virtual" style="transform: translateY(3740px); min-height: auto;"><div><div id="LC188" class="react-file-line html-div" data-testid="code-cell" data-line-number="188" inert="inert" style="position: relative;">    <span class="pl-c"># Format the best schedule for display</span></div></div></div><div data-key="188" class="child-of-line-57  react-code-text react-code-line-contents virtual" style="transform: translateY(3760px); min-height: auto;"><div><div id="LC189" class="react-file-line html-div" data-testid="code-cell" data-line-number="189" inert="inert" style="position: relative;">    <span class="pl-s1">final_schedule</span> <span class="pl-c1">=</span> []</div></div></div><div data-key="189" class="child-of-line-57  react-code-text react-code-line-contents virtual" style="transform: translateY(3780px); min-height: auto;"><div><div id="LC190" class="react-file-line html-div" data-testid="code-cell" data-line-number="190" inert="inert" style="position: relative;">    <span class="pl-k">for</span> <span class="pl-s1">surgery</span> <span class="pl-c1">in</span> <span class="pl-s1">best_schedule</span>:</div></div></div><div data-key="190" class="child-of-line-57  react-code-text react-code-line-contents virtual" style="transform: translateY(3800px); min-height: auto;"><div><div id="LC191" class="react-file-line html-div" data-testid="code-cell" data-line-number="191" inert="inert" style="position: relative;">        <span class="pl-s1">final_schedule</span>.<span class="pl-en">append</span>({</div></div></div><div data-key="191" class="child-of-line-57  react-code-text react-code-line-contents virtual" style="transform: translateY(3820px); min-height: auto;"><div><div id="LC192" class="react-file-line html-div" data-testid="code-cell" data-line-number="192" inert="inert" style="position: relative;">            <span class="pl-s">"surgery"</span>: <span class="pl-s1">surgery</span>[<span class="pl-s">"surgery"</span>],</div></div></div><div data-key="192" class="child-of-line-57  react-code-text react-code-line-contents virtual" style="transform: translateY(3840px); min-height: auto;"><div><div id="LC193" class="react-file-line html-div" data-testid="code-cell" data-line-number="193" inert="inert" style="position: relative;">            <span class="pl-s">"room"</span>: <span class="pl-s1">surgery</span>[<span class="pl-s">"room"</span>],</div></div></div><div data-key="193" class="child-of-line-57  react-code-text react-code-line-contents virtual" style="transform: translateY(3860px); min-height: auto;"><div><div id="LC194" class="react-file-line html-div" data-testid="code-cell" data-line-number="194" inert="inert" style="position: relative;">            <span class="pl-s">"slots"</span>: <span class="pl-s">f"<span class="pl-s1"><span class="pl-kos">{</span><span class="pl-s1">surgery</span>[<span class="pl-s">'start_slot'</span>]<span class="pl-kos">}</span></span> - <span class="pl-s1"><span class="pl-kos">{</span><span class="pl-s1">surgery</span>[<span class="pl-s">'end_slot'</span>]<span class="pl-kos">}</span></span>"</span>,</div></div></div><div data-key="194" class="child-of-line-57  react-code-text react-code-line-contents virtual" style="transform: translateY(3880px); min-height: auto;"><div><div id="LC195" class="react-file-line html-div" data-testid="code-cell" data-line-number="195" inert="inert" style="position: relative;">            <span class="pl-s">"staff"</span>: <span class="pl-s">', '</span>.<span class="pl-en">join</span>(<span class="pl-en">map</span>(<span class="pl-s1">str</span>, <span class="pl-s1">surgery</span>[<span class="pl-s">"staff"</span>])) <span class="pl-k">if</span> <span class="pl-s1">surgery</span>[<span class="pl-s">"staff"</span>] <span class="pl-k">else</span> <span class="pl-s">"No Staff Assigned"</span></div></div></div><div data-key="195" class="child-of-line-57  react-code-text react-code-line-contents virtual" style="transform: translateY(3900px); min-height: auto;"><div><div id="LC196" class="react-file-line html-div" data-testid="code-cell" data-line-number="196" inert="inert" style="position: relative;">        })</div></div></div><div data-key="196" class="child-of-line-57  react-code-text react-code-line-contents virtual" style="transform: translateY(3920px); min-height: auto;"><div><div id="LC197" class="react-file-line html-div" data-testid="code-cell" data-line-number="197" inert="inert" style="position: relative;">
</div></div></div><div data-key="197" class="react-code-text react-code-line-contents virtual" style="transform: translateY(3940px); min-height: auto;"><div><div id="LC198" class="react-file-line html-div" data-testid="code-cell" data-line-number="198" inert="inert" style="position: relative;">    <span class="pl-k">return</span> <span class="pl-s1">final_schedule</span></div></div></div><div data-key="198" class="react-code-text react-code-line-contents virtual" style="transform: translateY(3960px); min-height: auto;"><div><div id="LC199" class="react-file-line html-div" data-testid="code-cell" data-line-number="199" inert="inert" style="position: relative;">
</div></div></div><div data-key="199" class="react-code-text react-code-line-contents virtual" style="transform: translateY(3980px); min-height: auto;"><div><div id="LC200" class="react-file-line html-div" data-testid="code-cell" data-line-number="200" inert="inert" style="position: relative;"><span class="pl-c"># Run the Flask app</span></div></div></div><div data-key="200" class="react-code-text react-code-line-contents virtual" style="transform: translateY(4000px); min-height: auto;"><div><div id="LC201" class="react-file-line html-div" data-testid="code-cell" data-line-number="201" inert="inert" style="position: relative;"><span class="pl-k">if</span> <span class="pl-s1">__name__</span> <span class="pl-c1">==</span> <span class="pl-s">'__main__'</span>:</div></div></div><div data-key="201" class="react-code-text react-code-line-contents virtual" style="transform: translateY(4020px); min-height: auto;"><div><div id="LC202" class="react-file-line html-div" data-testid="code-cell" data-line-number="202" inert="inert" style="position: relative;">    <span class="pl-s1">app</span>.<span class="pl-en">run</span>(<span class="pl-s1">debug</span><span class="pl-c1">=</span><span class="pl-c1">True</span>)</div></div></div><div data-key="202" class="react-code-text react-code-line-contents virtual" style="transform: translateY(4040px); min-height: auto;"><div><div id="LC203" class="react-file-line html-div" data-testid="code-cell" data-line-number="203" inert="inert" style="position: relative;">
</div></div></div><div data-key="203" class="react-code-text react-code-line-contents virtual" style="transform: translateY(4060px); min-height: auto;"><div><div id="LC204" class="react-file-line html-div" data-testid="code-cell" data-line-number="204" inert="inert" style="position: relative;">
</div></div></div><div data-key="204" class="react-code-text react-code-line-contents virtual" style="transform: translateY(4080px); min-height: auto;"><div><div id="LC205" class="react-file-line html-div" data-testid="code-cell" data-line-number="205" inert="inert" style="position: relative;">
</div></div></div><div data-key="205" class="react-code-text react-code-line-contents virtual" style="transform: translateY(4100px); min-height: auto;"><div><div id="LC206" class="react-file-line html-div" data-testid="code-cell" data-line-number="206" inert="inert" style="position: relative;">
</div></div></div><div data-key="206" class="react-code-text react-code-line-contents virtual" style="transform: translateY(4120px); min-height: auto;"><div><div id="LC207" class="react-file-line html-div" data-testid="code-cell" data-line-number="207" inert="inert" style="position: relative;">        </div></div></div></div><button hidden="" data-hotkey="Control+a"></button></div></div><div class="Box-sc-g0xbh4-0 fXFeWj"><div class="Box-sc-g0xbh4-0 bvNKfH"></div></div></div></div><div id="copilot-button-container"></div></div><div id="highlighted-line-menu-container"></div></div></div></section></div></div><div class="Box-sc-g0xbh4-0 mgQhK"></div><div class="Box-sc-g0xbh4-0 YbKpH panel-content-narrow-styles inner-panel-content-not-narrow"><div id="symbols-pane"><div aria-labelledby="symbols-pane-header" class="Box-sc-g0xbh4-0 cxUsTr"><div class="Box-sc-g0xbh4-0 jXkPPw"><h2 id="symbols-pane-header" tabindex="-1" class="Box-sc-g0xbh4-0 hECgeo">Symbols</h2><button data-component="IconButton" type="button" aria-label="Close symbols" data-hotkey="Escape" class="Box-sc-g0xbh4-0 kybBdn prc-Button-ButtonBase-c50BI prc-Button-IconButton-szpyj" data-loading="false" data-no-visuals="true" data-size="medium" data-variant="invisible" aria-describedby=":R12qtal9lab:-loading-announcement"><svg aria-hidden="true" focusable="false" class="octicon octicon-x" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display:inline-block;user-select:none;vertical-align:text-bottom;overflow:visible"><path d="M3.72 3.72a.75.75 0 0 1 1.06 0L8 6.94l3.22-3.22a.749.749 0 0 1 1.275.326.749.749 0 0 1-.215.734L9.06 8l3.22 3.22a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L8 9.06l-3.22 3.22a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042L6.94 8 3.72 4.78a.75.75 0 0 1 0-1.06Z"></path></svg></button></div><div class="Box-sc-g0xbh4-0 cUqGUN">Find definitions and references for functions and other symbols in this file by clicking a symbol below or in the code.</div><span class="TextInputWrapper__TextInputBaseWrapper-sc-1mqhpbi-0 TextInputWrapper-sc-1mqhpbi-1 iHaEER brXZOx TextInput-wrapper" aria-busy="false"><span class="TextInput-icon" id=":R6qtal9lab:" aria-hidden="true"><svg aria-hidden="true" focusable="false" class="Octicon-sc-9kayk9-0" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display: inline-block; user-select: none; vertical-align: text-bottom; overflow: visible;"><path d="M.75 3h14.5a.75.75 0 0 1 0 1.5H.75a.75.75 0 0 1 0-1.5ZM3 7.75A.75.75 0 0 1 3.75 7h8.5a.75.75 0 0 1 0 1.5h-8.5A.75.75 0 0 1 3 7.75Zm3 4a.75.75 0 0 1 .75-.75h2.5a.75.75 0 0 1 0 1.5h-2.5a.75.75 0 0 1-.75-.75Z"></path></svg></span><input type="text" placeholder="Filter symbols" name="Filter symbols" aria-label="Filter symbols" aria-controls="filter-results" aria-expanded="true" aria-autocomplete="list" role="combobox" aria-describedby=":R6qtal9lab: :R6qtal9labH1:" data-component="input" class="UnstyledTextInput-sc-14ypya-0 kbCLEG" value=""><span class="TextInput-icon" id=":R6qtal9labH1:" aria-hidden="true"><div class="Box-sc-g0xbh4-0 gqhZpQ"><kbd>r</kbd></div></span></span><div class="Box-sc-g0xbh4-0 ccgkJf"><div id="filter-results" class="Box-sc-g0xbh4-0 kACRto"><span role="status" aria-live="polite" aria-atomic="true" class="_VisuallyHidden__VisuallyHidden-sc-11jhm7a-0 brGdpi"></span><ul role="tree" aria-label="Code Navigation" data-omit-spacer="false" data-truncate-text="true" class="TreeView__UlBox-sc-4ex6b6-0 gnOBko"><li class="PRIVATE_TreeView-item" tabindex="0" id="0app" role="treeitem" aria-labelledby=":R38qtal9lab:" aria-level="1" aria-selected="false"><div class="PRIVATE_TreeView-item-container" style="--level:1"><div style="grid-area:spacer;display:flex"><div style="width:100%;display:flex"></div></div><div id=":R38qtal9lab:" class="PRIVATE_TreeView-item-content"><span class="PRIVATE_TreeView-item-content-text"><div class="Box-sc-g0xbh4-0 cSURfY"><div class="Box-sc-g0xbh4-0 bTXewe"><div class="Box-sc-g0xbh4-0 izGIdz"></div><div class="Box-sc-g0xbh4-0 hFrmpR">const</div></div>  <div title="app" class="Truncate__StyledTruncate-sc-23o1d2-0 btDQYJ"><span>app</span></div></div></span></div></div></li><li class="PRIVATE_TreeView-item" tabindex="-1" id="1index" role="treeitem" aria-labelledby=":R58qtal9lab:" aria-level="1" aria-selected="false"><div class="PRIVATE_TreeView-item-container" style="--level:1"><div style="grid-area:spacer;display:flex"><div style="width:100%;display:flex"></div></div><div id=":R58qtal9lab:" class="PRIVATE_TreeView-item-content"><span class="PRIVATE_TreeView-item-content-text"><div class="Box-sc-g0xbh4-0 cSURfY"><div class="Box-sc-g0xbh4-0 bTXewe"><div class="Box-sc-g0xbh4-0 hXsfco"></div><div class="Box-sc-g0xbh4-0 bgxsom">func</div></div>  <div title="index" class="Truncate__StyledTruncate-sc-23o1d2-0 btDQYJ"><span>index</span></div></div></span></div></div></li><li class="PRIVATE_TreeView-item" tabindex="-1" id="2generate_schedule" role="treeitem" aria-labelledby=":R78qtal9lab:" aria-level="1" aria-selected="false"><div class="PRIVATE_TreeView-item-container" style="--level:1"><div style="grid-area:spacer;display:flex"><div style="width:100%;display:flex"></div></div><div id=":R78qtal9lab:" class="PRIVATE_TreeView-item-content"><span class="PRIVATE_TreeView-item-content-text"><div class="Box-sc-g0xbh4-0 cSURfY"><div class="Box-sc-g0xbh4-0 bTXewe"><div class="Box-sc-g0xbh4-0 hXsfco"></div><div class="Box-sc-g0xbh4-0 bgxsom">func</div></div>  <div title="generate_schedule" class="Truncate__StyledTruncate-sc-23o1d2-0 btDQYJ"><span>generate_schedule</span></div></div></span></div></div></li><li class="PRIVATE_TreeView-item" tabindex="-1" id="3genetic_algorithm" role="treeitem" aria-labelledby=":R98qtal9lab:" aria-level="1" aria-expanded="true" aria-selected="false"><div class="PRIVATE_TreeView-item-container" style="--level:1"><div style="grid-area:spacer;display:flex"><div style="width:100%;display:flex"></div></div><div class="PRIVATE_TreeView-item-toggle PRIVATE_TreeView-item-toggle--hover PRIVATE_TreeView-item-toggle--end"><svg aria-hidden="true" focusable="false" class="octicon octicon-chevron-down" viewBox="0 0 12 12" width="12" height="12" fill="currentColor" style="display:inline-block;user-select:none;vertical-align:text-bottom;overflow:visible"><path d="M6 8.825c-.2 0-.4-.1-.5-.2l-3.3-3.3c-.3-.3-.3-.8 0-1.1.3-.3.8-.3 1.1 0l2.7 2.7 2.7-2.7c.3-.3.8-.3 1.1 0 .3.3.3.8 0 1.1l-3.2 3.2c-.2.2-.4.3-.6.3Z"></path></svg></div><div id=":R98qtal9lab:" class="PRIVATE_TreeView-item-content"><span class="PRIVATE_TreeView-item-content-text"><div class="Box-sc-g0xbh4-0 cSURfY"><div class="Box-sc-g0xbh4-0 bTXewe"><div class="Box-sc-g0xbh4-0 hXsfco"></div><div class="Box-sc-g0xbh4-0 bgxsom">func</div></div>  <div title="genetic_algorithm" class="Truncate__StyledTruncate-sc-23o1d2-0 btDQYJ"><span>genetic_algorithm</span></div></div></span></div></div><ul role="group" style="list-style:none;padding:0;margin:0"><li class="PRIVATE_TreeView-item" tabindex="-1" id="0fitness" role="treeitem" aria-labelledby=":Rmp8qtal9lab:" aria-level="2" aria-selected="false"><div class="PRIVATE_TreeView-item-container" style="--level:2"><div style="grid-area:spacer;display:flex"><div style="width:100%;display:flex"><div class="PRIVATE_TreeView-item-level-line"></div></div></div><div id=":Rmp8qtal9lab:" class="PRIVATE_TreeView-item-content"><span class="PRIVATE_TreeView-item-content-text"><div class="Box-sc-g0xbh4-0 cSURfY"><div class="Box-sc-g0xbh4-0 bTXewe"><div class="Box-sc-g0xbh4-0 hXsfco"></div><div class="Box-sc-g0xbh4-0 bgxsom">func</div></div>  <div title="fitness" class="Truncate__StyledTruncate-sc-23o1d2-0 btDQYJ"><span>fitness</span></div></div></span></div></div></li><li class="PRIVATE_TreeView-item" tabindex="-1" id="1evolve" role="treeitem" aria-labelledby=":R16p8qtal9lab:" aria-level="2" aria-selected="false"><div class="PRIVATE_TreeView-item-container" style="--level:2"><div style="grid-area:spacer;display:flex"><div style="width:100%;display:flex"><div class="PRIVATE_TreeView-item-level-line"></div></div></div><div id=":R16p8qtal9lab:" class="PRIVATE_TreeView-item-content"><span class="PRIVATE_TreeView-item-content-text"><div class="Box-sc-g0xbh4-0 cSURfY"><div class="Box-sc-g0xbh4-0 bTXewe"><div class="Box-sc-g0xbh4-0 hXsfco"></div><div class="Box-sc-g0xbh4-0 bgxsom">func</div></div>  <div title="evolve" class="Truncate__StyledTruncate-sc-23o1d2-0 btDQYJ"><span>evolve</span></div></div></span></div></div></li></ul></li></ul></div></div></div></div></div></div> <!-- --> <!-- --> </div></div></div><div class="Box-sc-g0xbh4-0"></div></div></div></div></div><div id="find-result-marks-container" class="Box-sc-g0xbh4-0 cCoXib"></div><button hidden="" data-testid="" data-hotkey-scope="read-only-cursor-text-area" data-hotkey="Control+F6,Control+Shift+F6"></button><button hidden="" data-hotkey="Control+F6,Control+Shift+F6"></button></div> <!-- --> <!-- --> <script type="application/json" id="__PRIMER_DATA_:R0:__">{"resolvedServerColorMode":"day"}</script></div>
</react-app>




  </div>

</turbo-frame>

    </main>
  </div>

  </div>

          <footer class="footer pt-8 pb-6 f6 color-fg-muted p-responsive" role="contentinfo" hidden="">
  <h2 class="sr-only">Footer</h2>

  


  <div class="d-flex flex-justify-center flex-items-center flex-column-reverse flex-lg-row flex-wrap flex-lg-nowrap">
    <div class="d-flex flex-items-center flex-shrink-0 mx-2">
      <a aria-label="Homepage" title="GitHub" class="footer-octicon mr-2" href="https://github.com/">
        <svg aria-hidden="true" height="24" viewBox="0 0 24 24" version="1.1" width="24" data-view-component="true" class="octicon octicon-mark-github">
    <path d="M12.5.75C6.146.75 1 5.896 1 12.25c0 5.089 3.292 9.387 7.863 10.91.575.101.79-.244.79-.546 0-.273-.014-1.178-.014-2.142-2.889.532-3.636-.704-3.866-1.35-.13-.331-.69-1.352-1.18-1.625-.402-.216-.977-.748-.014-.762.906-.014 1.553.834 1.769 1.179 1.035 1.74 2.688 1.25 3.349.948.1-.747.402-1.25.733-1.538-2.559-.287-5.232-1.279-5.232-5.678 0-1.25.445-2.285 1.178-3.09-.115-.288-.517-1.467.115-3.048 0 0 .963-.302 3.163 1.179.92-.259 1.897-.388 2.875-.388.977 0 1.955.13 2.875.388 2.2-1.495 3.162-1.179 3.162-1.179.633 1.581.23 2.76.115 3.048.733.805 1.179 1.825 1.179 3.09 0 4.413-2.688 5.39-5.247 5.678.417.36.776 1.05.776 2.128 0 1.538-.014 2.774-.014 3.162 0 .302.216.662.79.547C20.709 21.637 24 17.324 24 12.25 24 5.896 18.854.75 12.5.75Z"></path>
</svg>
</a>
      <span>
        © 2024 GitHub,&nbsp;Inc.
      </span>
    </div>

    <nav aria-label="Footer">
      <h3 class="sr-only" id="sr-footer-heading">Footer navigation</h3>

      <ul class="list-style-none d-flex flex-justify-center flex-wrap mb-2 mb-lg-0" aria-labelledby="sr-footer-heading">

          <li class="mx-2">
            <a data-analytics-event="{&quot;category&quot;:&quot;Footer&quot;,&quot;action&quot;:&quot;go to Terms&quot;,&quot;label&quot;:&quot;text:terms&quot;}" href="https://docs.github.com/site-policy/github-terms/github-terms-of-service" data-view-component="true" class="Link--secondary Link">Terms</a>
          </li>

          <li class="mx-2">
            <a data-analytics-event="{&quot;category&quot;:&quot;Footer&quot;,&quot;action&quot;:&quot;go to privacy&quot;,&quot;label&quot;:&quot;text:privacy&quot;}" href="https://docs.github.com/site-policy/privacy-policies/github-privacy-statement" data-view-component="true" class="Link--secondary Link">Privacy</a>
          </li>

          <li class="mx-2">
            <a data-analytics-event="{&quot;category&quot;:&quot;Footer&quot;,&quot;action&quot;:&quot;go to security&quot;,&quot;label&quot;:&quot;text:security&quot;}" href="https://github.com/security" data-view-component="true" class="Link--secondary Link">Security</a>
          </li>

          <li class="mx-2">
            <a data-analytics-event="{&quot;category&quot;:&quot;Footer&quot;,&quot;action&quot;:&quot;go to status&quot;,&quot;label&quot;:&quot;text:status&quot;}" href="https://www.githubstatus.com/" data-view-component="true" class="Link--secondary Link">Status</a>
          </li>

          <li class="mx-2">
            <a data-analytics-event="{&quot;category&quot;:&quot;Footer&quot;,&quot;action&quot;:&quot;go to docs&quot;,&quot;label&quot;:&quot;text:docs&quot;}" href="https://docs.github.com/" data-view-component="true" class="Link--secondary Link">Docs</a>
          </li>

          <li class="mx-2">
            <a data-analytics-event="{&quot;category&quot;:&quot;Footer&quot;,&quot;action&quot;:&quot;go to contact&quot;,&quot;label&quot;:&quot;text:contact&quot;}" href="https://support.github.com/?tags=dotcom-footer" data-view-component="true" class="Link--secondary Link">Contact</a>
          </li>

          <li class="mx-2">
  <cookie-consent-link data-catalyst="">
    <button type="button" class="Link--secondary underline-on-hover border-0 p-0 color-bg-transparent" data-action="click:cookie-consent-link#showConsentManagement" data-analytics-event="{&quot;location&quot;:&quot;footer&quot;,&quot;action&quot;:&quot;cookies&quot;,&quot;context&quot;:&quot;subfooter&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;label&quot;:&quot;cookies_link_subfooter_footer&quot;}">
      Manage cookies
    </button>
  </cookie-consent-link>
</li>

<li class="mx-2">
  <cookie-consent-link data-catalyst="">
    <button type="button" class="Link--secondary underline-on-hover border-0 p-0 color-bg-transparent" data-action="click:cookie-consent-link#showConsentManagement" data-analytics-event="{&quot;location&quot;:&quot;footer&quot;,&quot;action&quot;:&quot;dont_share_info&quot;,&quot;context&quot;:&quot;subfooter&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;label&quot;:&quot;dont_share_info_link_subfooter_footer&quot;}">
      Do not share my personal information
    </button>
  </cookie-consent-link>
</li>

      </ul>
    </nav>
  </div>
</footer>




    <ghcc-consent id="ghcc" class="position-fixed bottom-0 left-0" style="z-index: 999999" data-initial-cookie-consent-allowed="" data-cookie-consent-required="false" data-catalyst=""></ghcc-consent>


  <div id="ajax-error-message" class="ajax-error-message flash flash-error" hidden="">
    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-alert">
    <path d="M6.457 1.047c.659-1.234 2.427-1.234 3.086 0l6.082 11.378A1.75 1.75 0 0 1 14.082 15H1.918a1.75 1.75 0 0 1-1.543-2.575Zm1.763.707a.25.25 0 0 0-.44 0L1.698 13.132a.25.25 0 0 0 .22.368h12.164a.25.25 0 0 0 .22-.368Zm.53 3.996v2.5a.75.75 0 0 1-1.5 0v-2.5a.75.75 0 0 1 1.5 0ZM9 11a1 1 0 1 1-2 0 1 1 0 0 1 2 0Z"></path>
</svg>
    <button type="button" class="flash-close js-ajax-error-dismiss" aria-label="Dismiss error">
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-x">
    <path d="M3.72 3.72a.75.75 0 0 1 1.06 0L8 6.94l3.22-3.22a.749.749 0 0 1 1.275.326.749.749 0 0 1-.215.734L9.06 8l3.22 3.22a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L8 9.06l-3.22 3.22a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042L6.94 8 3.72 4.78a.75.75 0 0 1 0-1.06Z"></path>
</svg>
    </button>
    You can’t perform that action at this time.
  </div>

    <template id="site-details-dialog"></template>

    <div class="Popover js-hovercard-content position-absolute" style="display: none; outline: none; top: 59.9844px !important; bottom: auto !important; left: 131.859px; z-index: 100;" aria-label="User Hovercard" role="region">
  <div class="Popover-message Popover-message--large Box color-shadow-large Popover-message--top-left" style="width:360px;"></div>
</div>

    <template id="snippet-clipboard-copy-button"></template>
<template id="snippet-clipboard-copy-button-unpositioned"></template>


    <style>
      .user-mention[href$="/Malaika-Mustafa"] {
        color: var(--color-user-mention-fg);
        background-color: var(--bgColor-attention-muted, var(--color-attention-subtle));
        border-radius: 2px;
        margin-left: -2px;
        margin-right: -2px;
      }
      .user-mention[href$="/Malaika-Mustafa"]:before,
      .user-mention[href$="/Malaika-Mustafa"]:after {
        content: '';
        display: inline-block;
        width: 2px;
      }
    </style>


    </div>

    <div id="js-global-screen-reader-notice" class="sr-only mt-n1" aria-live="polite" aria-atomic="true">AI_LABS/app.py at main · SumaikaImran/AI_LABS</div>
    <div id="js-global-screen-reader-notice-assertive" class="sr-only mt-n1" aria-live="assertive" aria-atomic="true"></div>
  


<div class="sr-only mt-n1" id="screenReaderAnnouncementDiv" role="alert" data-testid="screenReaderAnnouncement" aria-live="assertive">While the code is focused, press Alt+F1 for a menu of operations.</div><div id="__primerPortalRoot__" style="position: absolute; top: 0px; left: 0px;"><div style="position: relative; z-index: 1;"><span role="tooltip" aria-label="Copy path" data-visible-text="Copy path" aria-hidden="true" id=":Rdd9lab:" class="ControlledTooltip__TooltipBase-sc-b39269ff-0 bWQkSs tooltipped-nw" style="position: absolute; left: 473.906px; top: 122px;"></span></div></div></body></html>