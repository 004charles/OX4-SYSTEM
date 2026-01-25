#!/usr/bin/env bash
# build.sh - Atualizado para verificar requirements.txt

set -o errexit

echo "🚀 Iniciando build do Django ox4 transportes..."

# ------------------------------------------------------------
# 1. VERIFICAR requirements.txt
# ------------------------------------------------------------
if [ ! -f "requirements.txt" ]; then
    echo "⚠️  requirements.txt não encontrado, criando básico..."
    cat > requirements.txt << 'EOF'
Django>=4.0
gunicorn==21.2.0
whitenoise==6.6.0
psycopg2-binary==2.9.9
EOF
    echo "✅ requirements.txt básico criado"
fi

echo "📦 Conteúdo do requirements.txt:"
cat requirements.txt

# ------------------------------------------------------------
# 2. INSTALAÇÃO DE DEPENDÊNCIAS
# ------------------------------------------------------------
echo "📦 Instalando dependências Python..."
pip install --upgrade pip
pip install -r requirements.txt

# ------------------------------------------------------------
# 3. COLETAR ARQUIVOS ESTÁTICOS
# ------------------------------------------------------------
echo "🎨 Coletando arquivos estáticos..."

# Cria diretórios necessários
mkdir -p staticfiles
mkdir -p media  # se for usar uploads

# Verifica se tem o comando collectstatic
if python manage.py collectstatic --help > /dev/null 2>&1; then
    python manage.py collectstatic --noinput --clear
    echo "✅ Arquivos estáticos coletados"
else
    echo "⚠️  Comando collectstatic não disponível"
    echo "   Criando arquivo estático vazio para evitar erros..."
    mkdir -p staticfiles/admin
    echo "/* Empty static */" > staticfiles/empty.css
fi

# ------------------------------------------------------------
# 4. APLICAR MIGRAÇÕES (se houver banco)
# ------------------------------------------------------------
if [ -n "$DATABASE_URL" ] || [ -f "db.sqlite3" ]; then
    echo "🗄️  Aplicando migrações..."
    python manage.py migrate --noinput
else
    echo "ℹ️  Nenhum banco configurado, pulando migrações"
fi

echo "✅ Build concluído com sucesso!"