spons <- read.csv('/Users/colinmason/Desktop/yorglab/coding work/spons_mastersheet.csv')

spons_sub_tau <- subset(spons, !is.na(spons$tau) & spons$tau > 0)
spons_sub_tau$tau_log <- log(spons_sub_tau$tau)

library(lattice)

# Plots

boxplot(tau~sex, data=spons_sub_tau)
boxplot(tau~drug_applied, data=spons_sub_tau)
boxplot(tau~region_name, data=spons_sub_tau)

boxplot(tau_log~sex, data=spons_sub_tau)
boxplot(tau_log~drug_applied, data=spons_sub_tau)
boxplot(tau_log~region_name, data=spons_sub_tau)

# ANOVA test

tau_mod_sex <- aov(tau~sex,data=spons_sub_tau)
tau_mod_drug <- aov(tau~drug_applied, data=spons_sub_tau)
tau_mod_region_name <- aov(tau~region_name, data=spons_sub_tau)
anova(tau_mod_sex)
anova(tau_mod_drug)
anova(tau_mod_region_name)

log_mod_sex <- aov(tau_log~sex, data=spons_sub_tau)
log_mod_drug <- aov(tau_log~drug_applied, data=spons_sub_tau)
log_mod_region <- aov(tau_log~region_name, data=spons_sub_tau)


# Assumptions

spons_sub_tau$resids_sex <- resid(tau_mod_sex)
spons_sub_tau$resids_drug <- resid(tau_mod_drug)
spons_sub_tau$resids_region <- resid(tau_mod_region_name)

spons_sub_tau$resids_log_sex <- resid(log_mod_sex)
spons_sub_tau$resids_log_drug <- resid(log_mod_drug)
spons_sub_tau$resids_log_region <- resid(log_mod_region)


  # Normality
qqnorm(spons_sub_tau$resids_sex)
qqline(spons_sub_tau$resids_sex)

qqnorm(spons_sub_tau$resids_drug)
qqline(spons_sub_tau$resids_drug)

qqnorm(spons_sub_tau$resids_region)
qqline(spons_sub_tau$resids_region)



qqnorm(spons_sub_tau$resids_log_sex)
qqline(spons_sub_tau$resids_log_sex)

qqnorm(spons_sub_tau$resids_log_drug)
qqline(spons_sub_tau$resids_log_drug)

qqnorm(spons_sub_tau$resids_log_region)
qqline(spons_sub_tau$resids_log_region)



  # Independence
plot(spons_sub_tau$resids_sex, type='b')
abline(h=0)

plot(spons_sub_tau$resids_drug, type='b')
abline(h=0)

plot(spons_sub_tau$resids_region, type='b')
abline(h=0)

  # Mean Zero
mean(spons_sub_tau$resids_sex)
mean(spons_sub_tau$resids_drug)
mean(spons_sub_tau$resids_region)

  # Equal Variance
sd_trt_sex <- aggregate(tau~sex, data=spons_sub_tau, FUN=sd)

sd_trt_drug <- aggregate(tau~drug_applied, data=spons_sub_tau, FUN=sd)

sd_trt_region <- aggregate(tau~region_name, data=spons_sub_tau, FUN=sd)


