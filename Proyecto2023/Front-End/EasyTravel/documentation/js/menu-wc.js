'use strict';

customElements.define('compodoc-menu', class extends HTMLElement {
    constructor() {
        super();
        this.isNormalMode = this.getAttribute('mode') === 'normal';
    }

    connectedCallback() {
        this.render(this.isNormalMode);
    }

    render(isNormalMode) {
        let tp = lithtml.html(`
        <nav>
            <ul class="list">
                <li class="title">
                    <a href="index.html" data-type="index-link">easy-travel documentation</a>
                </li>

                <li class="divider"></li>
                ${ isNormalMode ? `<div id="book-search-input" role="search"><input type="text" placeholder="Type to search"></div>` : '' }
                <li class="chapter">
                    <a data-type="chapter-link" href="index.html"><span class="icon ion-ios-home"></span>Getting started</a>
                    <ul class="links">
                        <li class="link">
                            <a href="overview.html" data-type="chapter-link">
                                <span class="icon ion-ios-keypad"></span>Overview
                            </a>
                        </li>
                        <li class="link">
                            <a href="index.html" data-type="chapter-link">
                                <span class="icon ion-ios-paper"></span>README
                            </a>
                        </li>
                                <li class="link">
                                    <a href="dependencies.html" data-type="chapter-link">
                                        <span class="icon ion-ios-list"></span>Dependencies
                                    </a>
                                </li>
                                <li class="link">
                                    <a href="properties.html" data-type="chapter-link">
                                        <span class="icon ion-ios-apps"></span>Properties
                                    </a>
                                </li>
                    </ul>
                </li>
                    <li class="chapter modules">
                        <a data-type="chapter-link" href="modules.html">
                            <div class="menu-toggler linked" data-toggle="collapse" ${ isNormalMode ?
                                'data-target="#modules-links"' : 'data-target="#xs-modules-links"' }>
                                <span class="icon ion-ios-archive"></span>
                                <span class="link-name">Modules</span>
                                <span class="icon ion-ios-arrow-down"></span>
                            </div>
                        </a>
                        <ul class="links collapse " ${ isNormalMode ? 'id="modules-links"' : 'id="xs-modules-links"' }>
                            <li class="link">
                                <a href="modules/AppModule.html" data-type="entity-link" >AppModule</a>
                                    <li class="chapter inner">
                                        <div class="simple menu-toggler" data-toggle="collapse" ${ isNormalMode ?
                                            'data-target="#components-links-module-AppModule-611a04ff90ba57e0e48a739ec3a9f2e562b4b278758775c3727a2f28928f811a142cdf1aa0fbcdbe77040a5678be7bae7fb892e5001b0ab87268603631ff24ff"' : 'data-target="#xs-components-links-module-AppModule-611a04ff90ba57e0e48a739ec3a9f2e562b4b278758775c3727a2f28928f811a142cdf1aa0fbcdbe77040a5678be7bae7fb892e5001b0ab87268603631ff24ff"' }>
                                            <span class="icon ion-md-cog"></span>
                                            <span>Components</span>
                                            <span class="icon ion-ios-arrow-down"></span>
                                        </div>
                                        <ul class="links collapse" ${ isNormalMode ? 'id="components-links-module-AppModule-611a04ff90ba57e0e48a739ec3a9f2e562b4b278758775c3727a2f28928f811a142cdf1aa0fbcdbe77040a5678be7bae7fb892e5001b0ab87268603631ff24ff"' :
                                            'id="xs-components-links-module-AppModule-611a04ff90ba57e0e48a739ec3a9f2e562b4b278758775c3727a2f28928f811a142cdf1aa0fbcdbe77040a5678be7bae7fb892e5001b0ab87268603631ff24ff"' }>
                                            <li class="link">
                                                <a href="components/AppComponent.html" data-type="entity-link" data-context="sub-entity" data-context-id="modules" >AppComponent</a>
                                            </li>
                                            <li class="link">
                                                <a href="components/CabeceraComponent.html" data-type="entity-link" data-context="sub-entity" data-context-id="modules" >CabeceraComponent</a>
                                            </li>
                                            <li class="link">
                                                <a href="components/CuerpoComponent.html" data-type="entity-link" data-context="sub-entity" data-context-id="modules" >CuerpoComponent</a>
                                            </li>
                                            <li class="link">
                                                <a href="components/DestacadosComponent.html" data-type="entity-link" data-context="sub-entity" data-context-id="modules" >DestacadosComponent</a>
                                            </li>
                                            <li class="link">
                                                <a href="components/FiltroComponent.html" data-type="entity-link" data-context="sub-entity" data-context-id="modules" >FiltroComponent</a>
                                            </li>
                                            <li class="link">
                                                <a href="components/MenuComponent.html" data-type="entity-link" data-context="sub-entity" data-context-id="modules" >MenuComponent</a>
                                            </li>
                                            <li class="link">
                                                <a href="components/PieComponent.html" data-type="entity-link" data-context="sub-entity" data-context-id="modules" >PieComponent</a>
                                            </li>
                                        </ul>
                                    </li>
                            </li>
                            <li class="link">
                                <a href="modules/AppRoutingModule.html" data-type="entity-link" >AppRoutingModule</a>
                            </li>
                </ul>
                </li>
                        <li class="chapter">
                            <a data-type="chapter-link" href="routes.html"><span class="icon ion-ios-git-branch"></span>Routes</a>
                        </li>
                    <li class="chapter">
                        <a data-type="chapter-link" href="coverage.html"><span class="icon ion-ios-stats"></span>Documentation coverage</a>
                    </li>
                    <li class="divider"></li>
                    <li class="copyright">
                        Documentation generated using <a href="https://compodoc.app/" target="_blank">
                            <img data-src="images/compodoc-vectorise.png" class="img-responsive" data-type="compodoc-logo">
                        </a>
                    </li>
            </ul>
        </nav>
        `);
        this.innerHTML = tp.strings;
    }
});