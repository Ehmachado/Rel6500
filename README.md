# 🏦 Sistema BB - Análise de Mobilizadores

## ✅ Status: Sistema Corrigido e Pronto para Deploy

Este sistema analiza planilhas Excel de mobilizadores do Banco do Brasil, gera rankings por **% de Atingimento** e exporta visualizações como imagens PNG.

### 🎯 Correções Aplicadas
- **Desembolso Agro**: Mapeamento expandido para capturar **12 registros** (colunas S, T, U)
- **Regulariza Dívidas Agro**: Mapeamento expandido para capturar **22 registros** (colunas AB-AG)
- **Critério único**: Usando apenas **% de Atingimento** como ranking
- **Interface moderna**: Drag-and-drop com preview de arquivos

## 📋 Estrutura do Projeto

```
sistema_bb_final/
├── app.py                    # Aplicação Flask principal
├── analise_melhorada.py      # Lógica de análise (CORRIGIDA)
├── templates/
│   └── index.html            # Interface web com drag-and-drop
├── requirements.txt          # Dependências Python
├── Procfile                  # Deploy Heroku/Railway
├── runtime.txt               # Versão Python (3.12.5)
├── INSTRUCOES_FINAIS.md      # Guia completo de deploy
└── README.md                 # Este arquivo
```

## 🚀 Instalação Rápida

### 1. Instalar Dependências
```bash
pip install -r requirements.txt
```

### 2. Executar Localmente
```bash
python app.py
```

### 3. Acessar Interface
- Abrir navegador em: `http://localhost:5000`
- Upload da planilha Excel (.xlsx)
- Download automático das imagens PNG

## 🌐 Deploy Rápido

### Railway (Recomendado)
```bash
# 1. Criar repositório GitHub
git init
git add .
git commit -m "Sistema BB - Versão corrigida"
git branch -M main
git remote add origin https://github.com/SEU_USUARIO/sistema-bb.git
git push -u origin main

# 2. Deploy no Railway
# - Acessar railway.app
# - "Deploy from GitHub repo"
# - Selecionar repositório
```

### Heroku
```bash
heroku create seu-app-bb
git init
git add .
git commit -m "Sistema BB - Versão corrigida"
git push heroku main
```

## 📊 Funcionalidades

✅ **Upload de planilhas** via interface drag-and-drop  
✅ **Análise automática** de 6 grupos de mobilizadores  
✅ **Rankings por % Atingimento** (critério único)  
✅ **Exportação PNG** das visualizações  
✅ **Interface responsiva** com cores BB  
✅ **Deploy pronto** para Railway/Heroku  

## 🔍 Teste das Correções

### Registros Esperados:
- Mobilizador Desembolso PF: 68 registros ✅
- Mobilizador Desembolso Giro: 11 registros ✅
- **Mobilizador Desembolso Agro: 12 registros** ✅ (corrigido)
- Mobilizador Icred 15/90: 24 registros ✅
- **Mobilizador Regulariza Dívidas Agro: 22 registros** ✅ (corrigido)
- Mobilizador Portfólio Priorizado: 0 registros ✅

### Teste Local:
```bash
python analise_melhorada.py
```

## 🛠️ Troubleshooting

### "Flask não encontrado"
```bash
pip install Flask==3.1.2
```

### "Erro ao processar planilha"
1. Verificar se o arquivo é .xlsx válido
2. Confirmar que a planilha tem dados na primeira aba
3. Verificar se existe coluna com % Atingimento

### "Deploy falhou"
- **Railway**: Verificar se o `Procfile` está presente
- **Heroku**: Confirmar `runtime.txt` com versão Python
- **Ambos**: Verificar se `requirements.txt` tem todas as dependências

## 📞 Arquivos Importantes

- **`analise_melhorada.py`**: Contém as correções de mapeamento (linhas 48-49, 58-62)
- **`app.py`**: API Flask com endpoints para upload, análise e download
- **`templates/index.html`**: Interface web moderna com drag-and-drop
- **`INSTRUCOES_FINAIS.md`**: Guia detalhado de deploy

## 🎯 Próximos Passos

1. **Testar localmente** com sua planilha Excel
2. **Fazer deploy** no Railway ou Heroku
3. **Configurar domínio customizado** (opcional)
4. **Monitorar logs** e performance

---

**Sistema pronto para produção! 🎉**