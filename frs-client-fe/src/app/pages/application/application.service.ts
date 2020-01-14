import {Injectable} from '@angular/core';
import {getSelectedOrganizationId} from "../../store/organization/selectors";
import {combineLatest, merge, Observable, Subscription} from "rxjs";
import {ROUTERS_URL} from "../../data/routers-url.variable";
import {SetSelectedId} from "../../store/organization/action";
import {Organization} from "../../data/organization";
import {ActivatedRoute, Router} from "@angular/router";
import {OrganizationEnService} from "../../store/organization/organization-entitys.service";
import {Store} from "@ngrx/store";
import {AppState} from "../../store";
import {SelectRouterIdParam} from "../../store/router/selectors";
import {filter, map} from "rxjs/operators";
import {GetUserInfo} from "../../store/userInfo/action";
import {selectCurrentAppId} from "../../store/application/selectors";

@Injectable()
export class ApplicationService {
  selectedId$: Observable<any>;
  routId$: Observable<string>;
  private setInitialValueFromUrl$: Observable<any>;
  private redirectToOrganization$: Observable<any>;
  private setFirstOrganization$: Observable<any>;
  private setSelectedIdSubscription: Subscription;
  private redirectSubscription: Subscription;
  private organization$: Observable<Array<Organization>>;

  constructor(
    private router: Router,
    private route: ActivatedRoute,
    private store: Store<AppState>
  ) {}

  initUrlBindingStreams () {
    // this.organizationEnService.getAll();
    // this.store.dispatch(new GetUserInfo());
    //
    this.selectedId$ = this.store.select(selectCurrentAppId);
    this.routId$ = this.store.select(SelectRouterIdParam);

    this.routId$.subscribe(i => console.log('routerId$', i));
    this.selectedId$.subscribe(i => console.log('selectedId$', i));

    // this.setInitialValueFromUrl$ = combineLatest(this.selectedId$, this.organization$, this.routId$).pipe(
    //   filter(([selectedId, data, routerId]) => {
    //     return data.length && routerId && selectedId === null;
    //   }),
    //   filter(this.isValidId),
    //   map(([selectedId, data, routerId]) => routerId)
    // );
    //
    // this.setFirstOrganization$ = combineLatest(this.selectedId$, this.organization$, this.routId$).pipe(
    //   filter(([selectedId, data, routerId]) => {
    //     return data.length && routerId && selectedId === null;
    //   }),
    //   filter((data) => !this.isValidId(data)),
    //   map(([selectedId, data, routerId]) => data[0].id)
    // );
    //
    // this.redirectToOrganization$ = combineLatest(this.selectedId$, this.organization$, this.routId$).pipe(
    //   filter(([selectedId, data, routerId]) => {
    //     return !!(data.length && !routerId && selectedId === null);
    //   }),
    //   map(([selectedId, data, routerId]) => data[0].id)
    // );
    //
    // this.setSelectedIdSubscription = this.setInitialValueFromUrl$.subscribe(routerId => {
    //   this.store.dispatch(new SetSelectedId({selectId: routerId}));
    // });
    //
    // this.redirectSubscription = merge(
    //   this.redirectToOrganization$,
    //   this.setFirstOrganization$
    // ).subscribe(selectedId => {
    //   this.router.navigate([ROUTERS_URL.ORGANIZATION, selectedId])
    // })
  }

  unSubscribe () {
    // this.setSelectedIdSubscription.unsubscribe();
    // this.redirectSubscription.unsubscribe();
    // // clear selected Id for Organization
    // this.store.dispatch(new SetSelectedId({selectId: null}));
  }

  isValidId([selectedId, data, routerId]) {
    return data.some(array => array.id === routerId);
  }
}
