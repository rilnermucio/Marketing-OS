# Validation Guide — Marketing OS v6.3.0

Test cases pra validar que o orquestrador está dispatching corretamente nos workflows da v6.x.

## Como rodar os testes

1. Abra Claude Code numa pasta de teste (não no repo do plugin):
   ```bash
   mkdir ~/Code/test-marketing-os && cd $_
   claude
   ```

2. Pra cada caso abaixo, cole o briefing, observe **quais agents foram dispatched** e marque ✅ ou ❌.

3. Se algum dispatch falhar, abra issue com:
   - Versão do plugin (`/plugin` mostra)
   - Briefing usado
   - Agents que apareceram (esperados vs observados)

---

## Test cases

### Test 1 — Dispatch simples (workflow #1)

**Briefing:**
```
/marketing-os escreve 5 headlines pra meu curso de Python pra devs juniores
```

**Esperado:**
- ✅ Dispatch único: `mos-copy`
- ✅ Output: 5 headlines + 2-3 variações A/B
- ✅ Quality gates aplicados (sem `—`, sem "brutal", PT-BR correto)

---

### Test 2 — Dispatch paralelo (workflow #2)

**Briefing:**
```
/marketing-os tenho um curso novo de IA pra empreendedores BR, preciso de pesquisa de mercado + tom de marca + 5 headlines iniciais
```

**Esperado:**
- ✅ Dispatch paralelo (single message, 3 Agent calls): `mos-research` + `mos-brand` + `mos-copy`
- ✅ Outputs consolidados num único entregável

---

### Test 3 — Página de aplicação (workflow #5)

**Briefing:**
```
/marketing-os cria página de aplicação pra mentoria de marketing digital high-ticket (R$ 15.000)
```

**Esperado:**
- ✅ NÃO delegar direto a `frontend-design` ❌
- ✅ Dispatch paralelo Fase 1: `mos-funnel` + `mos-copy` + `mos-design`
- ✅ Brief consolidado entregue
- ✅ Pergunta se quer HTML/CSS de fato — só aí delega a `frontend-design`

**Como saber se está certo:** se o output só fala HTML/CSS sem mencionar "estrutura BOFU", "anti-avatar", "stack value", "paleta sugerida" → orquestrador pulou Fase 1 (bug).

---

### Test 4 — Carrossel completo (workflow #8)

**Briefing:**
```
/marketing-os cria um carrossel sobre 10 erros de copy que matam conversão, pra LinkedIn
```

**Esperado:**
- ✅ Dispatch paralelo: `mos-social` + `mos-copy` + `mos-design`
- ✅ Output: estrutura de slides + texto de cada slide + design spec + caption + hashtags + sugestão de enquete obrigatória

---

### Test 5 — VSL (workflow #9)

**Briefing:**
```
/marketing-os cria VSL completa pra produto de finanças (curso de R$ 1.997)
```

**Esperado:**
- ✅ Dispatch paralelo: `mos-storytelling` + `mos-copy` + `mos-video`
- ✅ Roteiro consolidado: arco narrativo + estrutura copy (big idea, mecanismo único, anti-avatar, stack value, garantia, FAQ) + ciência de retenção
- ✅ Disclaimer CVM aplicado automaticamente (nicho finanças)

---

### Test 6 — Briefing vago (protocolo de pergunta)

**Briefing:**
```
/marketing-os cria copy
```

**Esperado:**
- ✅ NÃO chuta nicho/avatar/plataforma
- ✅ Pergunta as 5 chaves de uma vez (numeradas):
  1. Nicho?
  2. Avatar?
  3. Ticket?
  4. Plataforma?
  5. Urgência?

---

### Test 7 — Memory persistente (project-scope)

**Setup:**
1. Pasta `~/Code/clientes/test-cliente-A`
2. Rodar Test 3 acima nessa pasta
3. Sair do Claude Code, voltar pra mesma pasta dias depois

**Briefing follow-up:**
```
/marketing-os gera 3 variações de headline pra essa página de aplicação
```

**Esperado:**
- ✅ `mos-copy` carrega memory de `.claude/agent-memory/marketing-os-mos-copy/`
- ✅ Não pergunta nicho/avatar/ticket de novo (já tem no memory)
- ✅ Headlines coerentes com posicionamento da sessão anterior

---

### Test 8 — Compliance regulatório

**Briefing (saúde):**
```
/marketing-os cria post Instagram pra clínica de nutrologia, com 3 dicas de saúde
```

**Esperado:**
- ✅ Detecta nicho saúde
- ✅ Aplica disclaimers automaticamente:
  - "Resultados variam"
  - CRM visível
  - Sem prometer "cura" ou "tratamento"

**Briefing (finanças):**
```
/marketing-os cria carrossel sobre fundo de investimento pra LinkedIn
```

**Esperado:**
- ✅ Detecta nicho finanças
- ✅ Adiciona "Rentabilidade passada não garante futura"
- ✅ Sem promessa de retorno

---

### Test 9 — Voice clone (assets/clones/)

**Briefing:**
```
/marketing-os escreve sales letter no estilo do Gary Halbert pra produto de finanças (curso R$ 997)
```

**Esperado:**
- ✅ `mos-copy` lê `assets/clones/halbert/`
- ✅ Output em estilo direto, agressivo, story-driven (típico Halbert)
- ✅ Disclaimer CVM aplicado (nicho finanças)

---

### Test 10 — Skill colision com `frontend-design`

**Setup:** plugins `frontend-design` e `marketing-os` instalados juntos.

**Briefing:**
```
/marketing-os preciso de uma página de aplicação BOFU pra mentoria de saúde
```

**Esperado:**
- ✅ Marketing-os assume controle (declarado em workflow #5)
- ✅ Dispatcha mos-funnel + mos-copy + mos-design ANTES de qualquer build
- ✅ Se user pediu HTML, entrega ao `frontend-design` Fase 2 com brief consolidado

**Se falhar:** o `frontend-design` interceptou direto sem passar pelos `mos-*`. Investigar dispatch priorities.

---

## Checklist de validação completa

Marque cada um após rodar:

- [ ] Test 1: dispatch simples (mos-copy)
- [ ] Test 2: dispatch paralelo (3 agents)
- [ ] Test 3: workflow #5 (página)
- [ ] Test 4: workflow #8 (carrossel)
- [ ] Test 5: workflow #9 (VSL)
- [ ] Test 6: protocolo de briefing vago
- [ ] Test 7: memory persistente
- [ ] Test 8: compliance regulatório (saúde + finanças)
- [ ] Test 9: voice clone (Halbert)
- [ ] Test 10: skill collision com frontend-design

Se 9+ passam: orquestração está saudável.
Se <8 passam: abrir issue com casos que falharam.

## Conhecidos limites

- **23 slash commands não dispatcham mos-* diretamente** (bug v6.3.0 conhecido). Workaround: use `/marketing-os` em linguagem natural em vez do command direto até v6.4.x.
- **Tier 2 smoke tests deferred:** rodar localmente com `python -m pytest scripts/tests/test_agents_smoke.py -v -m smoke` se quiser cobertura mais profunda.
