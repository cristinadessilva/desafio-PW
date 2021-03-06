$(function () {
    
    function showContent(nextPage) {
      $("#inicio").addClass("d-none");
      $("#tabela-pessoa").addClass("d-none");
      $("#tabela-salas").addClass("d-none");
      $("#tabela-cafes").addClass("d-none");
      $(`#${nextPage}`).removeClass("d-none");
    }

    $('#link-listar-pessoas').click(function () {
      mostrarPessoas();
    });

    $('#link-listar-salas').click(function () {
      mostrarSalas();
    });

    $('#link-listar-cafes').click(function () {
      mostrarCafes();
    });

    $("#link-inicial").click(function() {
      showContent("inicio");
    });

    $('#nav-brand').click(function () {
      showContent("inicio");
    });


    function mostrarPessoas() {
      $.ajax({
        url: 'http://localhost:5000/listar/pessoa',
        method: 'GET',
        dataType: 'json',
        success: listarPessoas,
        error: function () {
          alert('erro ao ler dados, verifique o backend');
        },
      });
  
      function listarPessoas(pessoas) {
        $("#tableBody").empty();
        showContent("tabela-pessoa");
        var linhas = '';
    
        for (pessoa of pessoas) {
          novaLinha = `<tr id="linha_${pessoa.id}">  
                            <td>${pessoa.id}</td> 
                            <td>${pessoa.nome+ " " +pessoa.sobrenome}</td>
                            <td>${pessoa.sala}</td> 
                            <td>${pessoa.cafe}</td> 
                          </tr>`;
          linhas += novaLinha;
          $('#tableBody').html(linhas);
        }
      }
    }
    
    $(document).on("click", "#btn-incluir", function() {
      const nome = $('#campo-nome').val();
      const sobrenome = $('#campo-sobrenome').val();
  
      const pessoaData = JSON.stringify({
        nome: nome,
        sobrenome: sobrenome,
      });
  
      $.ajax({
        url: 'http://localhost:5000/criar/pessoa',
        type: 'POST',
        contentType: 'application/json',
        dataType: 'json',
        data: pessoaData,
        success: criarPessoa,
        error: criarPessoaErro,
      });
  
      function criarPessoa(resposta) {
        if (resposta.result == 'ok') {
            alert('Pessoa adicionada com sucesso')
            $('#campo-nome').val('');
            $('#campo-sobrenome').val('');
        } 
        else {
            alert('Crie a sala e o espaço do café antes de cadastrar a pessoa!')
        }
      }
  
      function criarPessoaErro(resposta){
        alert('Erro na chamada do back-end')
      }
    });
    
    $('#modal-incluir-pessoa').on('hidden.bs.modal', function(e) {
      if (!$('#tabela-pessoa').hasClass('invisible')) {
        mostrarPessoas();
      }
    });
    
    function mostrarSalas() {
      $.ajax({
        url: 'http://localhost:5000/listar/sala',
        method: 'GET',
        dataType: 'json',
        success: listarSalas,
        error: function () {
          alert('erro ao ler dados, verifique o backend');
        },
      });
  
      function listarSalas(salas) {
        $("#corpoTabela").empty();
        showContent("tabela-salas");
        var linhas = '';
    
        for (sala of salas) {
          novaLinha = `<tr id="linha_${sala.id}">  
                            <td>${sala.id}</td> 
                            <td>${sala.nome_sala}</td> 
                            <td>${sala.lotacao}</td> 
                          </tr>`;
          linhas += novaLinha;
          $('#corpoTabela').html(linhas);
        }
      }
    }

    $(document).on("click", "#btn-incluir-sala", function() {
      const nome_sala = $('#campo-nome-sala').val();
      const lotacao = $('#campo-lotacao').val();
  
      const salaData = JSON.stringify({
        nome_sala: nome_sala,
        lotacao: lotacao,
      });
  
      $.ajax({
        url: 'http://localhost:5000/criar/sala',
        type: 'POST',
        contentType: 'application/json',
        dataType: 'json',
        data: salaData,
        success: criarSala,
        error: criarSalaErro,
      });
  
      function criarSala(resposta) {
        if (resposta.result == 'ok') {
            alert('Sala adicionada com sucesso')
            $('#campo-nome-sala').val('');
            $('#campo-lotacao').val('');
        } 
        else {
            alert('Erro na adição da sala!')
        }
      }
  
      function criarSalaErro(resposta){
        alert('Erro na chamada do back-end')
      }
    });
    
    $('#modal-incluir-sala').on('hidden.bs.modal', function(e) {
      if (!$('#tabela-salas').hasClass('invisible')) {
        mostrarSalas();
      }
    });
    
    function mostrarCafes() {
      $.ajax({
        url: 'http://localhost:5000/listar/cafe',
        method: 'GET',
        dataType: 'json',
        success: listarCafes,
        error: function () {
          alert('erro ao ler dados, verifique o backend');
        },
      });
  
      function listarCafes(cafes) {
        $("#corpoTabelaCafe").empty();
        showContent("tabela-cafes");
        var linhas = '';
    
        for (cafe of cafes) {
          novaLinha = `<tr id="linha_${cafe.id}">  
                            <td>${cafe.id}</td> 
                            <td>${cafe.nome_cafe}</td> 
                          </tr>`;
          linhas += novaLinha;
          $('#corpoTabelaCafe').html(linhas);
        }
      }
    }

    $(document).on("click", "#btn-incluir-cafe", function() {
      const nome_cafe = $('#campo-nome-cafe').val();
      const lotacao_cafe = $('#campo-lotacao-cafe').val();
  
      const cafeData = JSON.stringify({
        nome_cafe: nome_cafe,
        lotacao_cafe: lotacao_cafe,
      });
  
      $.ajax({
        url: 'http://localhost:5000/criar/cafe',
        type: 'POST',
        contentType: 'application/json',
        dataType: 'json',
        data: cafeData,
        success: criarCafe,
        error: criarCafeErro,
      });
  
      function criarCafe(resposta) {
        if (resposta.result == 'ok') {
            alert('Café adicionado com sucesso')
            $('#campo-nome-cafe').val('');
        } 
        else {
            alert('Erro na adição do café! Verifique se já não foi adicionada a quantidade máxima dos espaços do café.')
        }
      }
  
      function criarCafeErro(resposta){
        alert('Erro na chamada do back-end')
      }
    });
    
    $('#modal-incluir-cafe').on('hidden.bs.modal', function(e) {
      if (!$('#corpoTabelaCafe').hasClass('invisible')) {
        mostrarCafes();
      }
    });

    showContent("inicio");
  });
  
  
  