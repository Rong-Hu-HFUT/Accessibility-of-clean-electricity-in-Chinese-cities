**********能源转型 多元线性回归**********************
import excel "F:\数据和代码下载\不平等 数据\多元线性回归.xlsx", sheet("Sheet1") firstrow clear



gen lngdp_primary=ln(gdp_primary)
gen lngdp_second=ln(gdp_second)
gen lngdp_tertiary=ln(gdp_tertiary)
gen lnpop_city=ln(pop_city)
gen lnec_citypri=ln(ec_citypri)
gen lnec_citysec=ln(ec_citysec)
gen lnec_cityter=ln(ec_cityter)
gen lnec_pop=ln(ec_pop)
gen lnCleanpowertonsofstandardcoal=ln(Cleanpowertonsofstandardcoal) //人均清洁电力消耗
gen lnET=ln(ET)
gen lnIncomeYuan=ln(IncomeYuan)
gen lnClimate=ln(Climate)

global Varibles "lnET lnec_citypri lnec_citysec lnec_cityter lnec_pop lnIncomeYuan"
global Controls_5 "lngdp_primary  lngdp_second lngdp_tertiary lnpop_city lnClimate"
xtset id year
winsor2 ET, cuts(1 99) replace



qui xtreg lnCleanpowertonsofstandardcoal lnET i.id i.year ,fe cluster(id)
estadd local id "Yes",replace
estadd local year "Yes",replace
estadd local lnET "Yes",replace
// estadd local Weather_controls "Yes",replace
// estadd local Energy_controls "No",replace
// estadd local Economic_controls "No",replace


// esttab M1 using CP_ET.rtf, s(N r2_a id year lnET,label("N" "adj. R square" "City FE" "Year FE" "")) replace b(3) se ar2 noconstant star(* .10 ** .05 *** .01) keep($Mean_temp_bin)


qui xtreg lnCleanpowertonsofstandardcoal  $Varibles lngdp_primary i.year ,fe cluster(id)
estadd local id "Yes",replace
estadd local year "Yes",replace
estadd local province_year "No",replace
estadd local lngdp_primary "Yes",replace
estadd local lngdp_second "No",replace
estadd local lngdp_tertiary "No",replace
estadd local lnpop_city "No",replace
estadd local Climate "No",replace
eststo M1

qui xtreg lnCleanpowertonsofstandardcoal  $Varibles lngdp_second i.year ,fe cluster(id)
estadd local id "Yes",replace
estadd local year "Yes",replace
estadd local province_year "No",replace
estadd local lngdp_primary "No",replace
estadd local lngdp_second "Yes",replace
estadd local lngdp_tertiary "No",replace
estadd local lnpop_city "No",replace
estadd local Climate "No",replace
eststo M2

qui xtreg lnCleanpowertonsofstandardcoal  $Varibles lngdp_tertiary i.year ,fe cluster(id)
estadd local id "Yes",replace
estadd local year "Yes",replace
estadd local province_year "No",replace
estadd local lngdp_primary "No",replace
estadd local lngdp_second "No",replace
estadd local lngdp_tertiary "Yes",replace
estadd local lnpop_city "No",replace
estadd local Climate "No",replace
eststo M3

qui xtreg lnCleanpowertonsofstandardcoal  $Varibles lnpop_city i.year ,fe cluster(id)
estadd local id "Yes",replace
estadd local year "Yes",replace
estadd local province_year "No",replace
estadd local lngdp_primary "No",replace
estadd local lngdp_second "No",replace
estadd local lngdp_tertiary "No",replace
estadd local lnpop_city "Yes",replace
estadd local Climate "No",replace
eststo M4

qui xtreg lnCleanpowertonsofstandardcoal  $Varibles Climate i.year ,fe cluster(id)
estadd local id "Yes",replace
estadd local year "Yes",replace
estadd local province_year "No",replace
estadd local lngdp_primary "No",replace
estadd local lngdp_second "No",replace
estadd local lngdp_tertiary "No",replace
estadd local lnpop_city "No",replace
estadd local Climate "Yes",replace

eststo M5

esttab M1 M2 M3 M4 M5 using Controls.rtf, s(N r2_a id year province_year lngdp_primary  lngdp_second lngdp_tertiary lnpop_city Climate,label("N" "adj. R square" "City FE" "Year FE" "Province by year FE" "lngdp_primary" "lngdp_second" "lngdp_tertiary " "lnpop_city"  "Climate" )) replace b(3) se ar2 noconstant star(* .10 ** .05 *** .01) keep($Varibles)

qui xtreg lnCleanpowertonsofstandardcoal  $Varibles lngdp_primary lngdp_second i.year ,fe cluster(id)
estadd local id "Yes",replace
estadd local year "Yes",replace
estadd local province_year "No",replace
estadd local lngdp_primary "Yes",replace
estadd local lngdp_second "Yes",replace
estadd local lngdp_tertiary "No",replace
estadd local lnpop_city "No",replace
estadd local Climate "No",replace

eststo M6

qui xtreg lnCleanpowertonsofstandardcoal  $Varibles lngdp_primary lngdp_tertiary i.year ,fe cluster(id)
estadd local id "Yes",replace
estadd local year "Yes",replace
estadd local province_year "No",replace
estadd local lngdp_primary "Yes",replace
estadd local lngdp_second "No",replace
estadd local lngdp_tertiary "Yes",replace
estadd local lnpop_city "No",replace
estadd local Climate "No",replace

eststo M7

qui xtreg lnCleanpowertonsofstandardcoal  $Varibles lngdp_primary lnpop_city i.year ,fe cluster(id)
estadd local id "Yes",replace
estadd local year "Yes",replace
estadd local province_year "No",replace
estadd local lngdp_primary "Yes",replace
estadd local lngdp_second "No",replace
estadd local lngdp_tertiary "No",replace
estadd local lnpop_city "Yes",replace
estadd local Climate "No",replace

eststo M8

qui xtreg lnCleanpowertonsofstandardcoal  $Varibles lngdp_primary Climate i.year ,fe cluster(id)
estadd local id "Yes",replace
estadd local year "Yes",replace
estadd local province_year "No",replace
estadd local lngdp_primary "Yes",replace
estadd local lngdp_second "No",replace
estadd local lngdp_tertiary "No",replace
estadd local lnpop_city "No",replace
estadd local Climate "Yes",replace

eststo M9

qui xtreg lnCleanpowertonsofstandardcoal  $Varibles lngdp_second lngdp_tertiary i.year ,fe cluster(id)
estadd local id "Yes",replace
estadd local year "Yes",replace
estadd local province_year "No",replace
estadd local lngdp_primary "No",replace
estadd local lngdp_second "Yes",replace
estadd local lngdp_tertiary "Yes",replace
estadd local lnpop_city "No",replace
estadd local Climate "No",replace

eststo M10

qui xtreg lnCleanpowertonsofstandardcoal  $Varibles lngdp_second lnpop_city i.year ,fe cluster(id)
estadd local id "Yes",replace
estadd local year "Yes",replace
estadd local province_year "No",replace
estadd local lngdp_primary "No",replace
estadd local lngdp_second "Yes",replace
estadd local lngdp_tertiary "No",replace
estadd local lnpop_city "Yes",replace
estadd local Climate "No",replace

eststo M11

qui xtreg lnCleanpowertonsofstandardcoal  $Varibles lngdp_second Climate i.year ,fe cluster(id)
estadd local id "Yes",replace
estadd local year "Yes",replace
estadd local province_year "No",replace
estadd local lngdp_primary "No",replace
estadd local lngdp_second "Yes",replace
estadd local lngdp_tertiary "No",replace
estadd local lnpop_city "No",replace
estadd local Climate "Yes",replace

eststo M12

qui xtreg lnCleanpowertonsofstandardcoal  $Varibles lngdp_tertiary lnpop_city i.year ,fe cluster(id)
estadd local id "Yes",replace
estadd local year "Yes",replace
estadd local province_year "No",replace
estadd local lngdp_primary "No",replace
estadd local lngdp_second "No",replace
estadd local lngdp_tertiary "Yes",replace
estadd local lnpop_city "Yes",replace
estadd local Climate "No",replace

eststo M13

qui xtreg lnCleanpowertonsofstandardcoal  $Varibles lngdp_tertiary Climate i.year ,fe cluster(id)
estadd local id "Yes",replace
estadd local year "Yes",replace
estadd local province_year "No",replace
estadd local lngdp_primary "No",replace
estadd local lngdp_second "No",replace
estadd local lngdp_tertiary "Yes",replace
estadd local lnpop_city "No",replace
estadd local Climate "Yes",replace

eststo M14

esttab M6 M7 M8 M9 M10 M11 M12 M13 M14 using Controls2.rtf, s(N r2_a id year province_year lngdp_primary  lngdp_second lngdp_tertiary lnpop_city Climate,label("N" "adj. R square" "City FE" "Year FE" "Province by year FE" "lngdp_primary" "lngdp_second" "lngdp_tertiary " "lnpop_city"  "Climate" )) replace b(3) se ar2 noconstant star(* .10 ** .05 *** .01) keep($Varibles)

qui xtreg lnCleanpowertonsofstandardcoal  $Varibles lngdp_primary lngdp_second lngdp_tertiary i.year ,fe cluster(id)
estadd local id "Yes",replace
estadd local year "Yes",replace
estadd local province_year "No",replace
estadd local lngdp_primary "Yes",replace
estadd local lngdp_second "Yes",replace
estadd local lngdp_tertiary "Yes",replace
estadd local lnpop_city "No",replace
estadd local Climate "No",replace

eststo M15

qui xtreg lnCleanpowertonsofstandardcoal  $Varibles lngdp_primary lngdp_second lnpop_city i.year ,fe cluster(id)
estadd local id "Yes",replace
estadd local year "Yes",replace
estadd local province_year "No",replace
estadd local lngdp_primary "Yes",replace
estadd local lngdp_second "Yes",replace
estadd local lngdp_tertiary "No",replace
estadd local lnpop_city "Yes",replace
estadd local Climate "No",replace

eststo M16

qui xtreg lnCleanpowertonsofstandardcoal  $Varibles lngdp_primary lngdp_second Climate i.year ,fe cluster(id)
estadd local id "Yes",replace
estadd local year "Yes",replace
estadd local province_year "No",replace
estadd local lngdp_primary "Yes",replace
estadd local lngdp_second "Yes",replace
estadd local lngdp_tertiary "No",replace
estadd local lnpop_city "No",replace
estadd local Climate "Yes",replace

eststo M17

qui xtreg lnCleanpowertonsofstandardcoal  $Varibles lngdp_primary lngdp_tertiary lnpop_city i.year ,fe cluster(id)
estadd local id "Yes",replace
estadd local year "Yes",replace
estadd local province_year "No",replace
estadd local lngdp_primary "Yes",replace
estadd local lngdp_second "No",replace
estadd local lngdp_tertiary "Yes",replace
estadd local lnpop_city "Yes",replace
estadd local Climate "No",replace

eststo M18

qui xtreg lnCleanpowertonsofstandardcoal  $Varibles lngdp_primary lngdp_tertiary Climate i.year ,fe cluster(id)
estadd local id "Yes",replace
estadd local year "Yes",replace
estadd local province_year "No",replace
estadd local lngdp_primary "Yes",replace
estadd local lngdp_second "No",replace
estadd local lngdp_tertiary "Yes",replace
estadd local lnpop_city "No",replace
estadd local Climate "Yes",replace

eststo M19


qui xtreg lnCleanpowertonsofstandardcoal  $Varibles lngdp_second lngdp_tertiary lnpop_city i.year ,fe cluster(id)
estadd local id "Yes",replace
estadd local year "Yes",replace
estadd local province_year "No",replace
estadd local lngdp_primary "No",replace
estadd local lngdp_second "Yes",replace
estadd local lngdp_tertiary "Yes",replace
estadd local lnpop_city "Yes",replace
estadd local Climate "No",replace

eststo M20

qui xtreg lnCleanpowertonsofstandardcoal  $Varibles lngdp_second lngdp_tertiary Climate i.year ,fe cluster(id)
estadd local id "Yes",replace
estadd local year "Yes",replace
estadd local province_year "No",replace
estadd local lngdp_primary "No",replace
estadd local lngdp_second "Yes",replace
estadd local lngdp_tertiary "Yes",replace
estadd local lnpop_city "No",replace
estadd local Climate "Yes",replace

eststo M21

qui xtreg lnCleanpowertonsofstandardcoal  $Varibles lngdp_second lnpop_city Climate i.year ,fe cluster(id)
estadd local id "Yes",replace
estadd local year "Yes",replace
estadd local province_year "No",replace
estadd local lngdp_primary "No",replace
estadd local lngdp_second "Yes",replace
estadd local lngdp_tertiary "No",replace
estadd local lnpop_city "Yes",replace
estadd local Climate "Yes",replace

eststo M22

qui xtreg lnCleanpowertonsofstandardcoal  $Varibles lngdp_second lnpop_city Climate i.year ,fe cluster(id)
estadd local id "Yes",replace
estadd local year "Yes",replace
estadd local province_year "No",replace
estadd local lngdp_primary "No",replace
estadd local lngdp_second "No",replace
estadd local lngdp_tertiary "Yes",replace
estadd local lnpop_city "Yes",replace
estadd local Climate "Yes",replace

eststo M23

esttab M15 M16 M17 M18 M19 M20 M21 M22 M23 using Control3.rtf, s(N r2_a id year province_year lngdp_primary  lngdp_second lngdp_tertiary lnpop_city Climate,label("N" "adj. R square" "City FE" "Year FE" "Province by year FE" "lngdp_primary" "lngdp_second" "lngdp_tertiary " "lnpop_city"  "Climate" )) replace b(3) se ar2 noconstant star(* .10 ** .05 *** .01) keep($Varibles)

qui xtreg lnCleanpowertonsofstandardcoal  $Varibles lngdp_primary lngdp_second lngdp_tertiary lnpop_city i.year ,fe cluster(id)
estadd local id "Yes",replace
estadd local year "Yes",replace
estadd local province_year "No",replace
estadd local lngdp_primary "Yes",replace
estadd local lngdp_second "Yes",replace
estadd local lngdp_tertiary "Yes",replace
estadd local lnpop_city "Yes",replace
estadd local Climate "No",replace

eststo M24

qui xtreg lnCleanpowertonsofstandardcoal  $Varibles lngdp_primary lngdp_tertiary lnpop_city Climate i.year ,fe cluster(id)
estadd local id "Yes",replace
estadd local year "Yes",replace
estadd local province_year "No",replace
estadd local lngdp_primary "Yes",replace
estadd local lngdp_second "No",replace
estadd local lngdp_tertiary "Yes",replace
estadd local lnpop_city "Yes",replace
estadd local Climate "Yes",replace

eststo M25

qui xtreg lnCleanpowertonsofstandardcoal  $Varibles lngdp_primary lngdp_second lnpop_city Climate i.year ,fe cluster(id)
estadd local id "Yes",replace
estadd local year "Yes",replace
estadd local province_year "No",replace
estadd local lngdp_primary "Yes",replace
estadd local lngdp_second "Yes",replace
estadd local lngdp_tertiary "No",replace
estadd local lnpop_city "Yes",replace
estadd local Climate "Yes",replace

eststo M26

qui xtreg lnCleanpowertonsofstandardcoal  $Varibles lngdp_primary lngdp_second lngdp_tertiary Climate i.year ,fe cluster(id)
estadd local id "Yes",replace
estadd local year "Yes",replace
estadd local province_year "No",replace
estadd local lngdp_primary "Yes",replace
estadd local lngdp_second "Yes",replace
estadd local lngdp_tertiary "Yes",replace
estadd local lnpop_city "No",replace
estadd local Climate "Yes",replace

eststo M27

qui xtreg lnCleanpowertonsofstandardcoal  $Varibles lngdp_second lngdp_tertiary lnpop_city Climate i.year ,fe cluster(id)
estadd local id "Yes",replace
estadd local year "Yes",replace
estadd local province_year "No",replace
estadd local lngdp_primary "No",replace
estadd local lngdp_second "Yes",replace
estadd local lngdp_tertiary "Yes",replace
estadd local lnpop_city "Yes",replace
estadd local Climate "Yes",replace

eststo M28

qui xtreg lnCleanpowertonsofstandardcoal  $Varibles $Controls_5 i.year ,fe cluster(id)
estadd local id "Yes",replace
estadd local year "Yes",replace
estadd local province_year "No",replace
estadd local lngdp_primary "Yes",replace
estadd local lngdp_second "Yes",replace
estadd local lngdp_tertiary "Yes",replace
estadd local lnpop_city "Yes",replace
estadd local Climate "Yes",replace

eststo M29


esttab M24 M25 M26 M27 M28 M29 using Control4.rtf, s(N r2_a id year province_year lngdp_primary  lngdp_second lngdp_tertiary lnpop_city Climate,label("N" "adj. R square" "City FE" "Year FE" "Province by year FE" "lngdp_primary" "lngdp_second" "lngdp_tertiary " "lnpop_city"  "Climate" )) replace b(3) se ar2 noconstant star(* .10 ** .05 *** .01) keep($Varibles)



**********省-年固定效应**********************

egen province_year=group(pid year)
egen city_year=group(id year)

qui xtreg lnCleanpowertonsofstandardcoal  $Varibles lnpop_city i.id ,fe cluster(id)
estadd local id "Yes",replace
estadd local year "No",replace
estadd local province_year "No",replace
estadd local lngdp_primary "Yes",replace
estadd local lngdp_second "Yes",replace
estadd local lngdp_tertiary "Yes",replace
estadd local lnpop_city "Yes",replace
estadd local Climate "Yes",replace

eststo M33


qui xtreg lnCleanpowertonsofstandardcoal  $Varibles lnpop_city i.id#c.year ,fe cluster(id)
estadd local id "Yes",replace
estadd local year "Yes",replace
estadd local province_year "No",replace
estadd local lngdp_primary "Yes",replace
estadd local lngdp_second "Yes",replace
estadd local lngdp_tertiary "Yes",replace
estadd local lnpop_city "Yes",replace
estadd local Climate "Yes",replace

eststo M34
qui xtreg lnCleanpowertonsofstandardcoal  $Varibles lnpop_city i.pid,fe cluster(id)
estadd local id "No",replace
estadd local year "No",replace
estadd local province_year "Yes",replace
estadd local lngdp_primary "Yes",replace
estadd local lngdp_second "Yes",replace
estadd local lngdp_tertiary "Yes",replace
estadd local lnpop_city "Yes",replace
estadd local Climate "Yes",replace

eststo M35

qui xtreg lnCleanpowertonsofstandardcoal  $Varibles lnpop_city i.pid#c.year ,fe cluster(id)
estadd local id "No",replace
estadd local year "Yes",replace
estadd local province_year "Yes",replace
estadd local lngdp_primary "Yes",replace
estadd local lngdp_second "Yes",replace
estadd local lngdp_tertiary "Yes",replace
estadd local lnpop_city "Yes",replace
estadd local Climate "Yes",replace

eststo M36

qui xtreg lnCleanpowertonsofstandardcoal  $Varibles lnpop_city i.id i.pid#c.year ,fe cluster(id)
estadd local id "Yes",replace
estadd local year "Yes",replace
estadd local province_year "Yes",replace
estadd local lngdp_primary "Yes",replace
estadd local lngdp_second "Yes",replace
estadd local lngdp_tertiary "Yes",replace
estadd local lnpop_city "Yes",replace
estadd local Climate "Yes",replace

eststo M37


esttab M33 M34 M35 M36 M37 using pyear.rtf, s(N r2_a id year province_year lngdp_primary  lngdp_second lngdp_tertiary lnpop_city Climate,label("N" "adj. R square" "City FE" "Year FE" "Province FE" "lngdp_primary" "lngdp_second" "lngdp_tertiary " "lnpop_city"  "Climate" )) replace b(3) se ar2 noconstant star(* .10 ** .05 *** .01) keep($Varibles)



******************异质性分析


qui xtreg lnCleanpowertonsofstandardcoal  $Varibles lnpop_city i.id#c.year if Region==0,fe cluster(id) //东北
estadd local id "Yes",replace
estadd local year "Yes",replace
estadd local province_year "No",replace
estadd local lngdp_primary "Yes",replace
estadd local lngdp_second "Yes",replace
estadd local lngdp_tertiary "Yes",replace
estadd local lnpop_city "Yes",replace
estadd local Climate "Yes",replace
eststo m7

qui xtreg lnCleanpowertonsofstandardcoal  $Varibles lnpop_city i.id#c.year if Region==1,fe cluster(id) //西南
estadd local id "Yes",replace
estadd local year "Yes",replace
estadd local province_year "No",replace
estadd local lngdp_primary "Yes",replace
estadd local lngdp_second "Yes",replace
estadd local lngdp_tertiary "Yes",replace
estadd local lnpop_city "Yes",replace
estadd local Climate "Yes",replace
eststo m8

esttab m7 m8 using Heterogeneity.rtf, s(N r2_a id year province_year lngdp_primary  lngdp_second lngdp_tertiary lnpop_city Climate,label("N" "adj. R square" "City FE" "Year FE" "Province FE" "lngdp_primary" "lngdp_second" "lngdp_tertiary " "lnpop_city"  "Climate" )) replace b(3) se ar2 noconstant star(* .10 ** .05 *** .01) keep($Varibles)


















