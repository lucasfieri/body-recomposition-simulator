"""
Internationalization (i18n) module.
Supports: English (en), Português (pt).
"""

from __future__ import annotations

_TRANSLATIONS: dict[str, dict[str, str]] = {
    # ── App chrome ──────────────────────────────────────────────────
    "app_title": {
        "en": "💪 Body Recomposition Simulator",
        "pt": "💪 Simulador de Recomposição Corporal",
    },
    "app_caption": {
        "en": (
            "Evidence-based body composition projection using Mifflin-St Jeor, "
            "Katch-McArdle, adaptive thermogenesis, and Alan Aragon's muscle gain model."
        ),
        "pt": (
            "Projeção de composição corporal baseada em evidências usando Mifflin-St Jeor, "
            "Katch-McArdle, termogênese adaptativa e modelo de ganho muscular de Alan Aragon."
        ),
    },
    "language": {"en": "Language", "pt": "Idioma"},
    # ── Sidebar ─────────────────────────────────────────────────────
    "settings": {"en": "⚙️ Settings", "pt": "⚙️ Configurações"},
    "personal_info": {"en": "Personal Info", "pt": "Informações Pessoais"},
    "sex": {"en": "Sex", "pt": "Sexo"},
    "male": {"en": "Male", "pt": "Masculino"},
    "female": {"en": "Female", "pt": "Feminino"},
    "weight_kg": {"en": "Weight (kg)", "pt": "Peso (kg)"},
    "height_cm": {"en": "Height (cm)", "pt": "Altura (cm)"},
    "age": {"en": "Age", "pt": "Idade"},
    "sleep_hours": {"en": "Sleep (hours)", "pt": "Sono (horas)"},
    "sleep_help": {
        "en": "Sleep influences recovery, muscle protein synthesis, appetite regulation, and effective training output. Chronic short sleep can reduce lean mass retention and worsen adherence.",
        "pt": "O sono influencia recuperação, síntese proteica muscular, regulação do apetite e desempenho no treino. Privação crônica pode reduzir preservação de massa magra e piorar aderência.",
    },
    "training": {"en": "Training", "pt": "Treino"},
    "training_experience": {"en": "Training Experience", "pt": "Experiência de Treino"},
    "training_days_week": {"en": "Training days / week", "pt": "Dias de treino / semana"},
    "time_range": {"en": "Time Range", "pt": "Período"},
    "start": {"en": "Start", "pt": "Início"},
    "duration_preset": {"en": "Duration Preset", "pt": "Preset de Duração"},
    "custom": {"en": "Custom", "pt": "Personalizado"},
    "end": {"en": "End", "pt": "Fim"},
    "view": {"en": "View", "pt": "Visualização"},
    "granularity": {"en": "Granularity", "pt": "Granularidade"},
    "days": {"en": "Days", "pt": "Dias"},
    "weeks": {"en": "Weeks", "pt": "Semanas"},
    "months": {"en": "Months", "pt": "Meses"},
    "step": {"en": "Step", "pt": "Passo"},
    "optional_factors": {"en": "Optional Factors", "pt": "Fatores Opcionais"},
    "enable_optional_factors": {
        "en": "Enable optional behavior factors",
        "pt": "Habilitar fatores comportamentais opcionais",
    },
    "optional_factors_help": {
        "en": "Adds optional variables to improve realism: NEAT/steps, alcohol intake, and adherence.",
        "pt": "Adiciona variaveis opcionais para melhorar o realismo: NEAT/passos, consumo de alcool e aderencia.",
    },
    "neat_steps": {"en": "NEAT / Daily Steps", "pt": "NEAT / Passos Diarios"},
    "neat_steps_help": {
        "en": "Estimated average daily steps. More steps increase total daily energy expenditure (TDEE).",
        "pt": "Estimativa media de passos diarios. Mais passos aumentam o gasto energetico diario total (TDEE).",
    },
    "alcohol_drinks_week": {
        "en": "Alcohol Intake (drinks/week)",
        "pt": "Consumo de Alcool (doses/semana)",
    },
    "alcohol_drinks_help": {
        "en": "Approximate weekly alcoholic drinks. Alcohol adds calories and can reduce recovery quality.",
        "pt": "Numero aproximado de doses alcoolicas por semana. O alcool adiciona calorias e pode reduzir a recuperacao.",
    },
    "adherence_pct": {"en": "Estimated Adherence (%)", "pt": "Aderencia Estimada (%)"},
    "adherence_help": {
        "en": "How closely your real routine follows the plan. Lower adherence reduces effective calorie strategy outcomes.",
        "pt": "Quao perto sua rotina real segue o plano. Menor aderencia reduz o efeito pratico da estrategia calorica.",
    },
    # ── Training levels ─────────────────────────────────────────────
    "beginner": {"en": "Beginner (< 1 yr)", "pt": "Iniciante (< 1 ano)"},
    "intermediate": {"en": "Intermediate (1-3 yr)", "pt": "Intermediário (1-3 anos)"},
    "advanced": {"en": "Advanced (3+ yr)", "pt": "Avançado (3+ anos)"},
    # ── Tabs ────────────────────────────────────────────────────────
    "tab_cut": {"en": "🔻 Cut", "pt": "🔻 Cutting"},
    "tab_recomp": {"en": "⚖️ Recomp", "pt": "⚖️ Recomposição"},
    "tab_bulk": {"en": "🔺 Bulk", "pt": "🔺 Bulking"},
    "scenario_cut": {"en": "Cut", "pt": "Cutting"},
    "scenario_recomp": {"en": "Recomp", "pt": "Recomposição"},
    "scenario_bulk": {"en": "Bulk", "pt": "Bulking"},
    # ── Scenario panel ──────────────────────────────────────────────
    "configuration": {"en": "Configuration", "pt": "Configuração"},
    "protein_g_kg": {"en": "Protein (g/kg)", "pt": "Proteína (g/kg)"},
    "protein_help": {
        "en": "Evidence summary (ISSN 2017): active individuals benefit from ~1.4-2.0 g/kg/day; in cutting phases, 2.0-2.4 g/kg can help preserve lean mass.",
        "pt": "Resumo de evidencia (ISSN 2017): pessoas ativas se beneficiam de ~1.4-2.0 g/kg/dia; em cutting, 2.0-2.4 g/kg pode ajudar a preservar massa magra.",
    },
    "fat_pct_cal": {"en": "Fat (% of calories)", "pt": "Gordura (% das calorias)"},
    "fat_help": {
        "en": "Evidence summary: keep at least ~15-20% of calories from fat to support hormonal function and adherence.",
        "pt": "Resumo de evidencia: mantenha pelo menos ~15-20% das calorias vindas de gordura para suporte hormonal e aderencia.",
    },
    "calorie_delta": {"en": "Calorie delta (kcal/day)", "pt": "Delta calórico (kcal/dia)"},
    "calorie_delta_help": {
        "en": "Negative = deficit (fat loss), positive = surplus (muscle gain). Typical practical ranges: cut ~200-700 kcal/day, lean bulk ~100-350 kcal/day.",
        "pt": "Negativo = deficit (perda de gordura), positivo = superavit (ganho muscular). Faixas praticas comuns: cut ~200-700 kcal/dia, bulk limpo ~100-350 kcal/dia.",
    },
    "carb_cycling": {"en": "Carb Cycling", "pt": "Ciclo de Carboidratos"},
    "high_carb_days": {"en": "High-carb days/week", "pt": "Dias altos em carb/semana"},
    "carb_increase": {
        "en": "Carb increase on high days (%)",
        "pt": "Aumento de carb nos dias altos (%)",
    },
    "carb_cycling_help": {
        "en": "Redistributes carbs across the week while keeping weekly calories closer to plan.",
        "pt": "Redistribui carboidratos ao longo da semana mantendo as calorias semanais mais proximas do plano.",
    },
    "high_carb_days_help": {
        "en": "Choose how many days will have higher carbohydrate intake.",
        "pt": "Escolha quantos dias terao maior ingestao de carboidratos.",
    },
    "carb_increase_help": {
        "en": "How much carbs increase on high days relative to baseline.",
        "pt": "Quanto os carboidratos aumentam nos dias altos em relacao ao baseline.",
    },
    "profile_preset": {"en": "Profile Preset", "pt": "Preset de Perfil"},
    "profile_preset_help": {
        "en": "Applies preconfigured macro and calorie targets for common profiles.",
        "pt": "Aplica metas preconfiguradas de macros e calorias para perfis comuns.",
    },
    "profile_beginner": {"en": "Beginner", "pt": "Iniciante"},
    "profile_athlete": {"en": "Athlete", "pt": "Atleta"},
    "profile_aggressive_cut": {"en": "Aggressive Cut", "pt": "Cutting Agressivo"},
    "profile_light_recomp": {"en": "Light Recomp", "pt": "Recomposicao Leve"},
    "apply_profile_preset": {"en": "Apply Preset", "pt": "Aplicar Preset"},
    "profile_preset_applied": {
        "en": "Profile preset applied to calories and macros.",
        "pt": "Preset de perfil aplicado em calorias e macros.",
    },
    "profile_preset_disabled_in_goal": {
        "en": "Profile preset is disabled while Goal Mode is active (auto targets enabled).",
        "pt": "Preset de perfil desativado enquanto o Modo Meta estiver ativo (metas automáticas habilitadas).",
    },
    "goal_mode": {"en": "Goal Mode (Auto)", "pt": "Modo Meta (Auto)"},
    "goal_mode_help": {
        "en": "Automatically computes calorie delta and macro targets from your target BF%.",
        "pt": "Calcula automaticamente delta calórico e metas de macros a partir da sua meta de BF%.",
    },
    "goal_target_bf": {"en": "Target Body Fat (%)", "pt": "Meta de Gordura Corporal (%)"},
    "goal_strategy_cut": {"en": "Fat-loss focus", "pt": "Foco em perda de gordura"},
    "goal_strategy_gain": {"en": "Lean-gain focus", "pt": "Foco em ganho de massa magra"},
    "goal_strategy_maintain": {"en": "Recomposition/maintenance", "pt": "Recomposicao/manutencao"},
    "goal_mode_summary": {
        "en": "Current BF: {current:.1f}% -> Target BF: {target:.1f}%",
        "pt": "BF atual: {current:.1f}% -> BF meta: {target:.1f}%",
    },
    "goal_item_strategy": {"en": "Strategy", "pt": "Estratégia"},
    "goal_item_calorie_delta": {"en": "Calorie Delta", "pt": "Delta Calórico"},
    "goal_item_protein": {"en": "Protein Target", "pt": "Meta de Proteína"},
    "goal_item_fat": {"en": "Fat Target", "pt": "Meta de Gordura"},
    "goal_mode_reference": {
        "en": "Heuristic based on Aragon muscle-gain ceilings (2020), ISSN protein guidance (2017), and conservative surplus/deficit practice.",
        "pt": "Heurística baseada nos limites de ganho muscular de Aragon (2020), recomendações de proteína da ISSN (2017) e prática conservadora de superávit/déficit.",
    },
    # ── Metrics ─────────────────────────────────────────────────────
    "projected_results": {"en": "Projected Results", "pt": "Resultados Projetados"},
    "final_weight": {"en": "Final Weight", "pt": "Peso Final"},
    "final_bf": {"en": "Final BF%", "pt": "BF% Final"},
    "lean_mass": {"en": "Lean Mass", "pt": "Massa Magra"},
    "fat_mass": {"en": "Fat Mass", "pt": "Massa Gorda"},
    # ── Chart tabs ──────────────────────────────────────────────────
    "chart_weight": {"en": "📈 Weight", "pt": "📈 Peso"},
    "chart_composition": {"en": "🧬 Composition", "pt": "🧬 Composição"},
    "chart_metrics": {"en": "📊 Metrics", "pt": "📊 Métricas"},
    # ── Chart titles / labels ───────────────────────────────────────
    "weight_over_time": {"en": "Weight Over Time", "pt": "Peso ao Longo do Tempo"},
    "weight_kg_axis": {"en": "kg", "pt": "kg"},
    "weight_label": {"en": "Weight (kg)", "pt": "Peso (kg)"},
    "trend_7d": {"en": "7-day trend", "pt": "Tendência 7 dias"},
    "composition_over_time": {
        "en": "Body Composition Over Time",
        "pt": "Composição Corporal ao Longo do Tempo",
    },
    "fat_mass_label": {"en": "Fat Mass", "pt": "Massa Gorda"},
    "lean_mass_label": {"en": "Lean Mass", "pt": "Massa Magra"},
    "glycogen_water": {"en": "Glycogen + Water", "pt": "Glicogênio + Água"},
    "body_fat_pct": {"en": "Body Fat %", "pt": "% Gordura Corporal"},
    "avg_lean_change": {"en": "Avg Lean Mass Change", "pt": "Variação Média de Massa Magra"},
    "macro_split": {"en": "Macro Split", "pt": "Divisão de Macros"},
    "protein": {"en": "Protein", "pt": "Proteína"},
    "fat": {"en": "Fat", "pt": "Gordura"},
    "carbs": {"en": "Carbs", "pt": "Carboidratos"},
    # ── HuggingFace panel ───────────────────────────────────────────
    "hf_title": {
        "en": "🤖 Estimate Body Fat % with AI (HuggingFace MLP)",
        "pt": "🤖 Estimar % de Gordura com IA (HuggingFace MLP)",
    },
    "hf_install_msg": {
        "en": (
            "Install `huggingface-hub` and `tensorflow` to enable AI body fat estimation.\n\n"
            "```bash\nuv add huggingface-hub tensorflow\n```"
        ),
        "pt": (
            "Instale `huggingface-hub` e `tensorflow` para habilitar estimativa de gordura por IA.\n\n"
            "```bash\nuv add huggingface-hub tensorflow\n```"
        ),
    },
    "hf_description": {
        "en": (
            "Enter body circumference measurements for a more accurate body fat estimate "
            "using the [bodyfat-estimation-mlp](https://huggingface.co/ChanMeng666/bodyfat-estimation-mlp) model."
        ),
        "pt": (
            "Insira medidas de circunferência corporal para uma estimativa mais precisa de gordura "
            "usando o modelo [bodyfat-estimation-mlp](https://huggingface.co/ChanMeng666/bodyfat-estimation-mlp)."
        ),
    },
    "hf_use_ai": {"en": "Use AI estimation", "pt": "Usar estimativa por IA"},
    "hf_auto_convert": {
        "en": "Weight and height auto-converted from sidebar. Circumferences in cm.",
        "pt": "Peso e altura convertidos automaticamente da barra lateral. Circunferências em cm.",
    },
    "hf_weight_lbs": {"en": "Weight (lbs)", "pt": "Peso (lbs)"},
    "hf_height_in": {"en": "Height (inches)", "pt": "Altura (polegadas)"},
    "hf_neck": {"en": "Neck (cm)", "pt": "Pescoço (cm)"},
    "hf_chest": {"en": "Chest (cm)", "pt": "Peito (cm)"},
    "hf_abdomen": {"en": "Abdomen (cm)", "pt": "Abdômen (cm)"},
    "hf_hip": {"en": "Hip (cm)", "pt": "Quadril (cm)"},
    "hf_thigh": {"en": "Thigh (cm)", "pt": "Coxa (cm)"},
    "hf_wrist": {"en": "Wrist (cm)", "pt": "Pulso (cm)"},
    "hf_estimate_btn": {"en": "Estimate Body Fat %", "pt": "Estimar % de Gordura"},
    "hf_loading": {
        "en": "Loading model from HuggingFace...",
        "pt": "Carregando modelo do HuggingFace...",
    },
    "hf_missing_dependency": {
        "en": "Optional dependency missing: {package}. Install it to use AI body fat estimation.",
        "pt": "Dependencia opcional ausente: {package}. Instale para usar a estimativa de gordura por IA.",
    },
    "hf_tech_details": {
        "en": "Technical details: {error}",
        "pt": "Detalhes tecnicos: {error}",
    },
    "hf_error": {
        "en": "Could not load the HuggingFace model. Please verify your internet connection and dependency setup.",
        "pt": "Nao foi possivel carregar o modelo do HuggingFace. Verifique sua conexao com a internet e as dependencias.",
    },
    "hf_result": {"en": "Estimated Body Fat", "pt": "Gordura Corporal Estimada"},
    "hf_current_result": {
        "en": "Current AI estimate being used",
        "pt": "Estimativa atual por IA em uso",
    },
    "hf_result_caption": {
        "en": (
            "This estimate is based on the ChanMeng666/bodyfat-estimation-mlp neural network. "
            "For best results, measure circumferences accurately."
        ),
        "pt": (
            "Esta estimativa é baseada na rede neural ChanMeng666/bodyfat-estimation-mlp. "
            "Para melhores resultados, meça as circunferências com precisão."
        ),
    },
    "hf_prediction_failed": {"en": "Prediction failed", "pt": "Falha na predição"},
    "hf_prediction_failed_friendly": {
        "en": "Prediction failed. Please review the measurements and try again.",
        "pt": "Falha na predicao. Revise as medidas informadas e tente novamente.",
    },
    "hf_chart_applied_notice": {
        "en": "AI estimated body fat is being used as the initial value for simulation charts: {bf:.1f}%.",
        "pt": "A gordura corporal estimada por IA esta sendo usada como valor inicial nos graficos da simulacao: {bf:.1f}%.",
    },
    "bf_badge_active": {
        "en": "AI BF active: {bf:.1f}%",
        "pt": "BF por IA ativo: {bf:.1f}%",
    },
    "bf_badge_inactive": {
        "en": "AI BF inactive",
        "pt": "BF por IA inativo",
    },
    # ── Scientific references footer ────────────────────────────────
    "references_title": {
        "en": "📚 Scientific Evidence & References",
        "pt": "📚 Evidências Científicas & Referências",
    },
    "ref_mifflin_title": {
        "en": "Mifflin-St Jeor — Basal Metabolic Rate (BMR)",
        "pt": "Mifflin-St Jeor — Taxa Metabólica Basal (TMB)",
    },
    "ref_mifflin_desc": {
        "en": (
            "Gold-standard predictive equation for resting energy expenditure. "
            "Uses weight, height, age, and sex. More accurate than Harris-Benedict for most populations.\n\n"
            "**Formula (male):** BMR = 10 × weight(kg) + 6.25 × height(cm) − 5 × age − 5\n\n"
            "📄 Mifflin, M. D., St Jeor, S. T., Hill, L. A., Scott, B. J., Daugherty, S. A., & Koh, Y. O. (1990). "
            "*A new predictive equation for resting energy expenditure in healthy individuals.* "
            "The American Journal of Clinical Nutrition, 51(2), 241–247. "
            "[doi:10.1093/ajcn/51.2.241](https://doi.org/10.1093/ajcn/51.2.241)"
        ),
        "pt": (
            "Equação preditiva padrão-ouro para gasto energético de repouso. "
            "Utiliza peso, altura, idade e sexo. Mais precisa que Harris-Benedict para a maioria das populações.\n\n"
            "**Fórmula (masculino):** TMB = 10 × peso(kg) + 6.25 × altura(cm) − 5 × idade − 5\n\n"
            "📄 Mifflin, M. D., St Jeor, S. T., Hill, L. A., Scott, B. J., Daugherty, S. A., & Koh, Y. O. (1990). "
            "*A new predictive equation for resting energy expenditure in healthy individuals.* "
            "The American Journal of Clinical Nutrition, 51(2), 241–247. "
            "[doi:10.1093/ajcn/51.2.241](https://doi.org/10.1093/ajcn/51.2.241)"
        ),
    },
    "ref_katch_title": {
        "en": "Katch-McArdle — BMR from Lean Body Mass",
        "pt": "Katch-McArdle — TMB a Partir de Massa Magra",
    },
    "ref_katch_desc": {
        "en": (
            "BMR prediction based on lean body mass (LBM), more accurate for individuals with known body composition.\n\n"
            "**Formula:** BMR = 370 + 21.6 × LBM(kg)\n\n"
            "📄 McArdle, W. D., Katch, F. I., & Katch, V. L. (2010). "
            "*Exercise Physiology: Nutrition, Energy, and Human Performance* (7th ed.). "
            "Lippincott Williams & Wilkins."
        ),
        "pt": (
            "Predição de TMB baseada na massa corporal magra (MCM), mais precisa para indivíduos com composição corporal conhecida.\n\n"
            "**Fórmula:** TMB = 370 + 21.6 × MCM(kg)\n\n"
            "📄 McArdle, W. D., Katch, F. I., & Katch, V. L. (2010). "
            "*Exercise Physiology: Nutrition, Energy, and Human Performance* (7ª ed.). "
            "Lippincott Williams & Wilkins."
        ),
    },
    "ref_thermogenesis_title": {
        "en": "Adaptive Thermogenesis — Metabolic Adaptation",
        "pt": "Termogênese Adaptativa — Adaptação Metabólica",
    },
    "ref_thermogenesis_desc": {
        "en": (
            "During sustained caloric restriction, TDEE decreases beyond what is predicted by loss of body mass alone (5–15%). "
            "This simulator applies a progressive adaptation factor that ramps over ~30 days.\n\n"
            "📄 Trexler, E. T., Smith-Ryan, A. E., & Norton, L. E. (2014). "
            "*Metabolic adaptation to weight loss: implications for the athlete.* "
            "Journal of the International Society of Sports Nutrition, 11, 7. "
            "[doi:10.1186/1550-2783-11-7](https://doi.org/10.1186/1550-2783-11-7)"
        ),
        "pt": (
            "Durante restrição calórica sustentada, o TDEE diminui além do previsto pela perda de massa corporal (5–15%). "
            "Este simulador aplica um fator de adaptação progressivo que aumenta ao longo de ~30 dias.\n\n"
            "📄 Trexler, E. T., Smith-Ryan, A. E., & Norton, L. E. (2014). "
            "*Metabolic adaptation to weight loss: implications for the athlete.* "
            "Journal of the International Society of Sports Nutrition, 11, 7. "
            "[doi:10.1186/1550-2783-11-7](https://doi.org/10.1186/1550-2783-11-7)"
        ),
    },
    "ref_aragon_title": {
        "en": "Alan Aragon — Maximum Muscle Gain Rates",
        "pt": "Alan Aragon — Taxas Máximas de Ganho Muscular",
    },
    "ref_aragon_desc": {
        "en": (
            "Evidence-based ceiling for natural muscle gain based on training experience:\n"
            "- **Beginner (<1 yr):** ~1.0–1.5% body weight/month\n"
            "- **Intermediate (1-3 yr):** ~0.5–1.0%/month\n"
            "- **Advanced (3+ yr):** ~0.25–0.5%/month\n\n"
            "📄 Aragon, A. A., & Schoenfeld, B. J. (2020). "
            "*Magnitude and Composition of the Energy Surplus for Maximizing Muscle Hypertrophy: Implications for Bodybuilding and Physique Athletes.* "
            "Strength & Conditioning Journal, 42(5), 79–86. "
            "[doi:10.1519/SSC.0000000000000539](https://doi.org/10.1519/SSC.0000000000000539)"
        ),
        "pt": (
            "Teto baseado em evidências para ganho muscular natural por nível de experiência:\n"
            "- **Iniciante (<1 ano):** ~1.0–1.5% do peso corporal/mês\n"
            "- **Intermediário (1-3 anos):** ~0.5–1.0%/mês\n"
            "- **Avançado (3+ anos):** ~0.25–0.5%/mês\n\n"
            "📄 Aragon, A. A., & Schoenfeld, B. J. (2020). "
            "*Magnitude and Composition of the Energy Surplus for Maximizing Muscle Hypertrophy: Implications for Bodybuilding and Physique Athletes.* "
            "Strength & Conditioning Journal, 42(5), 79–86. "
            "[doi:10.1519/SSC.0000000000000539](https://doi.org/10.1519/SSC.0000000000000539)"
        ),
    },
    "ref_pratio_title": {
        "en": "Forbes P-Ratio — Energy Partitioning",
        "pt": "Forbes P-Ratio — Particionamento Energético",
    },
    "ref_pratio_desc": {
        "en": (
            "Determines how much of an energy deficit comes from fat vs lean tissue. "
            "Higher body fat → more fat mobilised, less muscle lost.\n\n"
            "📄 Forbes, G. B. (1987). "
            "*Lean body mass–body fat interrelationships in humans.* "
            "Nutrition Reviews, 45(8), 225–231. "
            "[doi:10.1111/j.1753-4887.1987.tb07489.x](https://doi.org/10.1111/j.1753-4887.1987.tb07489.x)"
        ),
        "pt": (
            "Determina quanto de um déficit energético vem de gordura vs tecido magro. "
            "Maior % de gordura → mais gordura mobilizada, menos músculo perdido.\n\n"
            "📄 Forbes, G. B. (1987). "
            "*Lean body mass–body fat interrelationships in humans.* "
            "Nutrition Reviews, 45(8), 225–231. "
            "[doi:10.1111/j.1753-4887.1987.tb07489.x](https://doi.org/10.1111/j.1753-4887.1987.tb07489.x)"
        ),
    },
    "ref_tef_title": {
        "en": "TEF — Thermic Effect of Food",
        "pt": "TEF — Efeito Térmico dos Alimentos",
    },
    "ref_tef_desc": {
        "en": (
            "Energy cost of digesting macronutrients: Protein ~20–30%, Carbs ~5–10%, Fat ~0–3%. "
            "High-protein diets have a metabolic advantage through higher TEF.\n\n"
            "📄 Westerterp, K. R. (2004). "
            "*Diet induced thermogenesis.* "
            "Nutrition & Metabolism, 1, 5. "
            "[doi:10.1186/1743-7075-1-5](https://doi.org/10.1186/1743-7075-1-5)"
        ),
        "pt": (
            "Custo energético da digestão dos macronutrientes: Proteína ~20–30%, Carboidratos ~5–10%, Gordura ~0–3%. "
            "Dietas ricas em proteína têm vantagem metabólica pelo maior TEF.\n\n"
            "📄 Westerterp, K. R. (2004). "
            "*Diet induced thermogenesis.* "
            "Nutrition & Metabolism, 1, 5. "
            "[doi:10.1186/1743-7075-1-5](https://doi.org/10.1186/1743-7075-1-5)"
        ),
    },
    "ref_deurenberg_title": {
        "en": "Deurenberg — Body Fat % from BMI",
        "pt": "Deurenberg — % Gordura Corporal a Partir do IMC",
    },
    "ref_deurenberg_desc": {
        "en": (
            "Prediction formula relating BMI to body fat percentage, accounting for age and sex. "
            "Used as fallback when direct measurements are unavailable.\n\n"
            "**Formula:** BF% = 1.20 × BMI + 0.23 × age − 10.8 × sex − 5.4\n\n"
            "📄 Deurenberg, P., Weststrate, J. A., & Seidell, J. C. (1991). "
            "*Body mass index as a measure of body fatness: age- and sex-specific prediction formulas.* "
            "British Journal of Nutrition, 65(2), 105–114. "
            "[doi:10.1079/BJN19910073](https://doi.org/10.1079/BJN19910073)"
        ),
        "pt": (
            "Fórmula de predição que relaciona IMC com percentual de gordura corporal, considerando idade e sexo. "
            "Usada como fallback quando medições diretas não estão disponíveis.\n\n"
            "**Fórmula:** BF% = 1.20 × IMC + 0.23 × idade − 10.8 × sexo − 5.4\n\n"
            "📄 Deurenberg, P., Weststrate, J. A., & Seidell, J. C. (1991). "
            "*Body mass index as a measure of body fatness: age- and sex-specific prediction formulas.* "
            "British Journal of Nutrition, 65(2), 105–114. "
            "[doi:10.1079/BJN19910073](https://doi.org/10.1079/BJN19910073)"
        ),
    },
    "ref_issn_title": {
        "en": "ISSN Position Stand — Protein & Exercise",
        "pt": "Posicionamento ISSN — Proteína & Exercício",
    },
    "ref_issn_desc": {
        "en": (
            "International Society of Sports Nutrition position on optimal protein intake for active individuals: "
            "1.4–2.0 g/kg/day, with 0.25–0.40 g/kg per meal to maximise muscle protein synthesis.\n\n"
            "📄 Jäger, R., Kerksick, C. M., Campbell, B. I., et al. (2017). "
            "*International Society of Sports Nutrition Position Stand: protein and exercise.* "
            "Journal of the International Society of Sports Nutrition, 14, 20. "
            "[doi:10.1186/s12970-017-0177-8](https://doi.org/10.1186/s12970-017-0177-8)"
        ),
        "pt": (
            "Posicionamento da International Society of Sports Nutrition sobre ingestão proteica ideal para indivíduos ativos: "
            "1.4–2.0 g/kg/dia, com 0.25–0.40 g/kg por refeição para maximizar síntese proteica muscular.\n\n"
            "📄 Jäger, R., Kerksick, C. M., Campbell, B. I., et al. (2017). "
            "*International Society of Sports Nutrition Position Stand: protein and exercise.* "
            "Journal of the International Society of Sports Nutrition, 14, 20. "
            "[doi:10.1186/s12970-017-0177-8](https://doi.org/10.1186/s12970-017-0177-8)"
        ),
    },
    "ref_neat_title": {
        "en": "NEAT / Daily Steps — Energy Expenditure",
        "pt": "NEAT / Passos Diários — Gasto Energético",
    },
    "ref_neat_desc": {
        "en": (
            "NEAT (non-exercise activity thermogenesis) is a major contributor to inter-individual differences in daily energy expenditure and fat-gain resistance. "
            "This simulator optionally adjusts TDEE using daily steps as a practical NEAT proxy.\n\n"
            "📄 Levine, J. A., Eberhardt, N. L., & Jensen, M. D. (1999). "
            "*Role of nonexercise activity thermogenesis in resistance to fat gain in humans.* "
            "Science, 283(5399), 212-214. "
            "[doi:10.1126/science.283.5399.212](https://doi.org/10.1126/science.283.5399.212)"
        ),
        "pt": (
            "NEAT (termogênese de atividade não-exercício) é um grande determinante das diferenças individuais no gasto energético diário e na resistência ao ganho de gordura. "
            "Este simulador ajusta opcionalmente o TDEE usando passos diários como proxy prático de NEAT.\n\n"
            "📄 Levine, J. A., Eberhardt, N. L., & Jensen, M. D. (1999). "
            "*Role of nonexercise activity thermogenesis in resistance to fat gain in humans.* "
            "Science, 283(5399), 212-214. "
            "[doi:10.1126/science.283.5399.212](https://doi.org/10.1126/science.283.5399.212)"
        ),
    },
    "ref_alcohol_title": {
        "en": "Alcohol Intake — Recovery and Muscle Protein Synthesis",
        "pt": "Consumo de Álcool — Recuperação e Síntese Proteica Muscular",
    },
    "ref_alcohol_desc": {
        "en": (
            "Post-exercise alcohol ingestion can impair myofibrillar protein synthesis, potentially affecting recovery and adaptation. "
            "The simulator includes an optional alcohol factor that adds calories and applies a conservative recovery penalty.\n\n"
            "📄 Parr, E. B., Camera, D. M., Areta, J. L., et al. (2014). "
            "*Alcohol ingestion impairs maximal post-exercise rates of myofibrillar protein synthesis following a single bout of concurrent training.* "
            "PLOS ONE, 9(2), e88384. "
            "[doi:10.1371/journal.pone.0088384](https://doi.org/10.1371/journal.pone.0088384)"
        ),
        "pt": (
            "A ingestão de álcool após o treino pode prejudicar a síntese proteica miofibrilar, afetando recuperação e adaptação. "
            "O simulador inclui um fator opcional de álcool que adiciona calorias e aplica uma penalidade conservadora de recuperação.\n\n"
            "📄 Parr, E. B., Camera, D. M., Areta, J. L., et al. (2014). "
            "*Alcohol ingestion impairs maximal post-exercise rates of myofibrillar protein synthesis following a single bout of concurrent training.* "
            "PLOS ONE, 9(2), e88384. "
            "[doi:10.1371/journal.pone.0088384](https://doi.org/10.1371/journal.pone.0088384)"
        ),
    },
    "ref_adherence_title": {
        "en": "Diet Adherence — Real-World Outcome Predictor",
        "pt": "Aderência à Dieta — Preditor de Resultado no Mundo Real",
    },
    "ref_adherence_desc": {
        "en": (
            "Across named diet strategies, adherence is one of the strongest predictors of weight-loss outcomes in free-living settings. "
            "This simulator includes an adherence percentage to scale effective strategy implementation.\n\n"
            "📄 Dansinger, M. L., Gleason, J. A., Griffith, J. L., Selker, H. P., & Schaefer, E. J. (2005). "
            "*Comparison of the Atkins, Ornish, Weight Watchers, and Zone diets for weight loss and heart disease risk reduction: a randomized trial.* "
            "JAMA, 293(1), 43-53. "
            "[doi:10.1001/jama.293.1.43](https://doi.org/10.1001/jama.293.1.43)"
        ),
        "pt": (
            "Entre diferentes estratégias dietéticas, a aderência é um dos preditores mais fortes de perda de peso em condições de vida real. "
            "Este simulador inclui um percentual de aderência para escalar a implementação efetiva da estratégia.\n\n"
            "📄 Dansinger, M. L., Gleason, J. A., Griffith, J. L., Selker, H. P., & Schaefer, E. J. (2005). "
            "*Comparison of the Atkins, Ornish, Weight Watchers, and Zone diets for weight loss and heart disease risk reduction: a randomized trial.* "
            "JAMA, 293(1), 43-53. "
            "[doi:10.1001/jama.293.1.43](https://doi.org/10.1001/jama.293.1.43)"
        ),
    },
    "ref_hf_title": {
        "en": "HuggingFace MLP — Body Fat Estimation",
        "pt": "HuggingFace MLP — Estimativa de Gordura Corporal",
    },
    "ref_hf_desc": {
        "en": (
            "Multi-layer perceptron neural network for body fat prediction from anthropometric measurements (R² ≈ 0.97). "
            "Used optionally for more accurate initial body fat estimation.\n\n"
            "🤗 [ChanMeng666/bodyfat-estimation-mlp](https://huggingface.co/ChanMeng666/bodyfat-estimation-mlp)"
        ),
        "pt": (
            "Rede neural perceptron multicamadas para predição de gordura corporal a partir de medidas antropométricas (R² ≈ 0.97). "
            "Usada opcionalmente para uma estimativa inicial de gordura mais precisa.\n\n"
            "🤗 [ChanMeng666/bodyfat-estimation-mlp](https://huggingface.co/ChanMeng666/bodyfat-estimation-mlp)"
        ),
    },
}


def t(key: str, lang: str = "pt") -> str:
    """Get translation for *key* in the given *lang*. Falls back to English."""
    entry = _TRANSLATIONS.get(key)
    if entry is None:
        return key
    return entry.get(lang, entry.get("en", key))
