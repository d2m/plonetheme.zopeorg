(function($) {
    $(document).ready(function() {
        var tagName = 'h2.accordion';
        if ($("#parent-fieldname-text " + tagName).length>0 && !$("#document-base-edit").length>0) {
            $(tagName).each(function () {
                var $this = $(this).next();
                $this.add($this.nextUntil(tagName)).wrapAll('<div></div>');
            });
            $("#parent-fieldname-text").children().wrapAll('<div id="accordion"></div>');
            $("#accordion").accordion({ header: tagName, autoHeight: false });
        }
    });
})(jQuery);
