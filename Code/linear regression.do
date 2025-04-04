import excel "Data.xlsx", sheet("Sheet1") firstrow clear

gen lngdp_primary=ln(gdp_primary)
gen lngdp_second=ln(gdp_second)
gen lngdp_tertiary=ln(gdp_tertiary)
gen lnpop_city=ln(pop_city)
gen lnec_citypri=ln(ec_citypri)
gen lnec_citysec=ln(ec_citysec)
gen lnec_cityter=ln(ec_cityter)
gen lnec_pop=ln(ec_pop)
gen lnCleanpowertonsofstandardcoal=ln(Cleanpowertonsofstandardcoal)
gen lnET=ln(ET)
gen lnIncomeYuan=ln(IncomeYuan)
gen lnClimate=ln(Climate)

global Varibles "lnET lnec_citypri lnec_citysec lnec_cityter lnec_pop lnIncomeYuan"
global Controls_5 "lngdp_primary  lngdp_second lngdp_tertiary lnpop_city lnClimate"
xtset id year
winsor2 ET, cuts(1 99) replace


egen province_year=group(pid year)
egen city_year=group(id year)


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


esttab M34 M35 M36 M37 using pyear.rtf, s(N r2_a id year province_year lngdp_primary  lngdp_second lngdp_tertiary lnpop_city Climate,label("N" "adj. R square" "City FE" "Year FE" "Province FE" "lngdp_primary" "lngdp_second" "lngdp_tertiary " "lnpop_city"  "Climate" )) replace b(3) se ar2 noconstant star(* .10 ** .05 *** .01) keep($Varibles)
















