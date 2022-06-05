# Lucene Workshop Manual

### Portuguese Version 
Esse é um projeto básico para entendimento sobre como o Apache Lucene funciona, escrito por __Fábio Bragada__ e __Hugo Figueira__, alunos da Universidade Federal da Bahia. Esse trabalho é parte da nota final para disciplina __MATC96__, lecionada pelo professor __Frederico Durão__ .

### Dependências

- Python3
- Apache Lucene

### Como instalar

Após instalar o python3, você precisará instalar [lupyne](https://github.com/coady/lupyne) via comando `pip`:
```console
% pip install lupyne
```

### Executar código

Com todas as dependências satisfeitas, só precisa rodar o comando abaixo:
```console
% python3 src/main.py
```
e o programa vai mostrar um menu com todas as ações possíveis: `insert`, `search` and `exit`.
```console
|=================================================|
| Select an action:
|-------------------------------------------------|
| ➕ (i) Insert a new registry to Lucene
| 🔍 (s) Search for a registry by a term on Lucene
| 🚪 (e) Exit from program
|=================================================|
| What do you want to do?
```

### Insering novos registros
Selecione a ação `i`, e em seguida digite `Title`, `Artist` e `Lyrics`  do seu registro. O mesmo será indexado pelo Lucene.

```console
|-------------------------------------------------|
| ➕ Type data of the registry
├─ Title: One Step Closer
├─ Artist: Linkin Park
├─ Lyrics: I cannot take this anymore I'm saying everything I've said before
|-------------------------------------------------|
|  ✅ Registry successfully added!
|-------------------------------------------------|
```

### Search for registries
Once you already created a registry before, you can type `s` to search a registry by a term. You can fill multiple terms for you query separated by a blank space or comma, and all registries related to your registry will be returned.

```console
|-------------------------------------------------|
| 🔍 Type terms, you want to search:
├─    linkin anymore
|=================================================|
| ✅ Your query returned 3 results
|=================================================|
[1]
| id:            1654391946
| title:         One Step Closer
| artist:        Linkin Park
| lyrics:        I cannot take this anymore I'm saying everything I've said before
|-------------------------------------------------|
```

If there's not registries related to your search term, an error message will be returned.

```console
|-------------------------------------------------|
| 🔍 Type terms, you want to search:
├─    ufba
|-------------------------------------------------|
| ❌ There's no records with the term 'ufba'.
|=================================================|
```



#English Version
This is a basic project to understand how Apache Lucene works, built by __Fábio Braga__ and __Hugo Figueira__ from __Federal University of Bahia__. This is part of final grade for __MATC96__ course, taught by __Professor Frederico Durão__.





### Dependencies

- Python3
- Apache Lucene

### How to install

Once you have python3, you need to install [lupyne](https://github.com/coady/lupyne) via `pip` command:
```console
% pip install lupyne
```

### Running

With all dependencies installed, you just need to run the command below
```console
% python3 src/main.py
```
and program menu will show up with all available actions: `insert`, `search` and `exit`.

```console
|=================================================|
| Select an action:
|-------------------------------------------------|
| ➕ (i) Insert a new registry to Lucene
| 🔍 (s) Search for a registry by a term on Lucene
| 🚪 (e) Exit from program
|=================================================|
| What do you want to do?
```

### Inserting a new registry
Selecting the action `i`, you need to type the `Title`, `Artist` and `Lyrics` of your registry. Your registry will be indexed by Apache Lucene.

```console
|-------------------------------------------------|
| ➕ Type data of the registry
├─ Title: One Step Closer
├─ Artist: Linkin Park
├─ Lyrics: I cannot take this anymore I'm saying everything I've said before
|-------------------------------------------------|
|  ✅ Registry successfully added!
|-------------------------------------------------|
```

### Search for registries
Once you already created a registry before, you can type `s` to search a registry by a term. You can fill multiple terms for you query separated by a blank space or comma, and all registries related to your registry will be returned.

```console
|-------------------------------------------------|
| 🔍 Type terms, you want to search:
├─    linkin anymore
|=================================================|
| ✅ Your query returned 3 results
|=================================================|
[1]
| id:            1654391946
| title:         One Step Closer
| artist:        Linkin Park
| lyrics:        I cannot take this anymore I'm saying everything I've said before
|-------------------------------------------------|
```

If there's not registries related to your search term, an error message will be returned.

```console
|-------------------------------------------------|
| 🔍 Type terms, you want to search:
├─    ufba
|-------------------------------------------------|
| ❌ There's no records with the term 'ufba'.
|=================================================|
```
