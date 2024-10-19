# Generated by Django 3.2.24 on 2024-06-25 21:45
import django.db.models.deletion
import django.db.models.manager
import django.utils.timezone
from django.db import migrations
from django.db import models

import morango.models.fields.crypto
import morango.models.fields.uuids


# morango.migrations.0020_postgres_fix_nullable
# is ignored in this squashed migration, as it is replaced by
# the original change made via an edit to the prior migration.
# morango.migrations.0021_store_partition_index_create
# is turned into a non-concurrent index creation operation, as
# this will only be run on a fresh database.


class Migration(migrations.Migration):

    replaces = [
        ("morango", "0001_initial"),
        ("morango", "0002_auto_20170511_0400"),
        ("morango", "0003_auto_20170519_0543"),
        ("morango", "0004_auto_20170520_2112"),
        ("morango", "0005_auto_20170629_2139"),
        ("morango", "0006_instanceidmodel_system_id"),
        ("morango", "0007_auto_20171018_1615"),
        ("morango", "0008_auto_20171114_2217"),
        ("morango", "0009_auto_20171205_0252"),
        ("morango", "0010_auto_20171206_1615"),
        ("morango", "0011_sharedkey"),
        ("morango", "0012_auto_20180927_1658"),
        ("morango", "0013_auto_20190627_1513"),
        ("morango", "0014_syncsession_extra_fields"),
        ("morango", "0015_auto_20200508_2104"),
        ("morango", "0016_store_deserialization_error"),
        ("morango", "0017_store_last_transfer_session_id"),
        ("morango", "0018_auto_20210714_2216"),
        ("morango", "0019_auto_20220113_1807"),
        ("morango", "0020_postgres_fix_nullable"),
        ("morango", "0021_store_partition_index_create"),
        ("morango", "0022_rename_instance_fields"),
        ("morango", "0023_add_instance_id_fields"),
        ("morango", "0024_auto_20240129_1757"),
    ]

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="DatabaseIDModel",
            fields=[
                (
                    "id",
                    morango.models.fields.uuids.UUIDField(
                        editable=False, primary_key=True, serialize=False
                    ),
                ),
                ("current", models.BooleanField(default=True)),
                (
                    "date_generated",
                    models.DateTimeField(default=django.utils.timezone.now),
                ),
                ("initial_instance_id", models.CharField(blank=True, max_length=32)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="DatabaseMaxCounter",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("instance_id", morango.models.fields.uuids.UUIDField()),
                ("counter", models.IntegerField()),
                ("partition", models.CharField(default="", max_length=128)),
            ],
            options={
                "abstract": False,
                "unique_together": {("instance_id", "partition")},
            },
        ),
        migrations.CreateModel(
            name="DeletedModels",
            fields=[
                (
                    "id",
                    morango.models.fields.uuids.UUIDField(
                        primary_key=True, serialize=False
                    ),
                ),
                ("profile", models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name="Store",
            fields=[
                ("serialized", models.TextField(blank=True)),
                ("deleted", models.BooleanField(default=False)),
                ("last_saved_instance", morango.models.fields.uuids.UUIDField()),
                ("last_saved_counter", models.IntegerField()),
                ("model_name", models.CharField(max_length=40)),
                ("profile", models.CharField(max_length=40)),
                ("partition", models.TextField()),
                (
                    "id",
                    morango.models.fields.uuids.UUIDField(
                        primary_key=True, serialize=False
                    ),
                ),
                ("conflicting_serialized_data", models.TextField(blank=True)),
                ("_self_ref_fk", models.CharField(blank=True, max_length=32)),
                ("dirty_bit", models.BooleanField(default=False)),
                (
                    "source_id",
                    models.CharField(
                        max_length=96,
                    ),
                ),
                ("hard_deleted", models.BooleanField(default=False)),
                ("deserialization_error", models.TextField(blank=True)),
                (
                    "last_transfer_session_id",
                    morango.models.fields.uuids.UUIDField(
                        blank=True, db_index=True, default=None, null=True
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="SyncSession",
            fields=[
                (
                    "id",
                    morango.models.fields.uuids.UUIDField(
                        primary_key=True, serialize=False
                    ),
                ),
                (
                    "start_timestamp",
                    models.DateTimeField(default=django.utils.timezone.now),
                ),
                ("last_activity_timestamp", models.DateTimeField(blank=True)),
                ("active", models.BooleanField(default=True)),
                (
                    "connection_kind",
                    models.CharField(
                        choices=[('network', 'Network'), ('disk', 'Disk')],
                        max_length=10,
                    ),
                ),
                (
                    "connection_path",
                    models.CharField(
                        max_length=1000,
                    ),
                ),
                ("is_server", models.BooleanField(default=False)),
                ("client_instance", models.TextField(default="{}")),
                ("client_ip", models.CharField(blank=True, max_length=100)),
                (
                    "profile",
                    models.CharField(
                        max_length=40,
                    ),
                ),
                ("server_instance", models.TextField(default="{}")),
                ("server_ip", models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="TransferSession",
            fields=[
                (
                    "id",
                    morango.models.fields.uuids.UUIDField(
                        primary_key=True, serialize=False
                    ),
                ),
                ("filter", models.TextField()),
                ("push", models.BooleanField()),
                ("active", models.BooleanField(default=True)),
                ("records_total", models.IntegerField(blank=True, null=True)),
                (
                    "sync_session",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="morango.syncsession",
                    ),
                ),
                (
                    "last_activity_timestamp",
                    models.DateTimeField(
                        blank=True,
                    ),
                ),
                ("client_fsic", models.TextField(blank=True, default="{}")),
                ("records_transferred", models.IntegerField(default=0)),
                ("server_fsic", models.TextField(blank=True, default="{}")),
                (
                    "start_timestamp",
                    models.DateTimeField(default=django.utils.timezone.now),
                ),
                (
                    "bytes_received",
                    models.BigIntegerField(blank=True, default=0, null=True),
                ),
                (
                    "bytes_sent",
                    models.BigIntegerField(blank=True, default=0, null=True),
                ),
                (
                    "transfer_stage",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("initializing", "Initializing"),
                            ("serializing", "Serializing"),
                            ("queuing", "Queuing"),
                            ("transferring", "Transferring"),
                            ("dequeuing", "Dequeuing"),
                            ("deserializing", "Deserializing"),
                            ("cleanup", "Cleanup"),
                        ],
                        max_length=20,
                        null=True,
                    ),
                ),
                (
                    "transfer_stage_status",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("pending", "Pending"),
                            ("started", "Started"),
                            ("completed", "Completed"),
                            ("errored", "Errored"),
                        ],
                        max_length=20,
                        null=True,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ScopeDefinition",
            fields=[
                ("profile", models.CharField(max_length=20)),
                ("version", models.IntegerField()),
                (
                    "id",
                    models.CharField(max_length=20, primary_key=True, serialize=False),
                ),
                ("description", models.TextField()),
                ("read_filter_template", models.TextField()),
                ("write_filter_template", models.TextField()),
                ("read_write_filter_template", models.TextField()),
                (
                    "primary_scope_param_key",
                    models.CharField(blank=True, max_length=20),
                ),
            ],
        ),
        migrations.CreateModel(
            name="RecordMaxCounterBuffer",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("instance_id", morango.models.fields.uuids.UUIDField()),
                ("counter", models.IntegerField()),
                ("model_uuid", morango.models.fields.uuids.UUIDField(db_index=True)),
                (
                    "transfer_session",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="morango.transfersession",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Certificate",
            fields=[
                (
                    "id",
                    morango.models.fields.uuids.UUIDField(
                        primary_key=True, serialize=False
                    ),
                ),
                ("profile", models.CharField(max_length=20)),
                ("scope_version", models.IntegerField()),
                ("scope_params", models.TextField()),
                ("public_key", morango.models.fields.crypto.PublicKeyField()),
                ("serialized", models.TextField()),
                ("signature", models.TextField()),
                (
                    "private_key",
                    morango.models.fields.crypto.PrivateKeyField(blank=True, null=True),
                ),
                ("lft", models.PositiveIntegerField(editable=False)),
                ("rght", models.PositiveIntegerField(editable=False)),
                ("tree_id", models.PositiveIntegerField(db_index=True, editable=False)),
                ("level", models.PositiveIntegerField(editable=False)),
                (
                    "parent",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="morango.certificate",
                    ),
                ),
                (
                    "scope_definition",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="morango.scopedefinition",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="RecordMaxCounter",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("instance_id", morango.models.fields.uuids.UUIDField()),
                ("counter", models.IntegerField()),
                (
                    "store_model",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="morango.store"
                    ),
                ),
            ],
            options={
                "unique_together": {("store_model", "instance_id")},
            },
        ),
        migrations.AlterModelManagers(
            name="certificate",
            managers=[
                ("objects", django.db.models.manager.Manager()),
            ],
        ),
        migrations.AlterField(
            model_name="certificate",
            name="id",
            field=morango.models.fields.uuids.UUIDField(
                editable=False, primary_key=True, serialize=False
            ),
        ),
        migrations.AlterModelManagers(
            name="certificate",
            managers=[],
        ),
        migrations.RenameField(
            model_name="certificate",
            old_name="private_key",
            new_name="_private_key",
        ),
        migrations.AlterField(
            model_name="certificate",
            name="_private_key",
            field=morango.models.fields.crypto.PrivateKeyField(
                blank=True, db_column="private_key", null=True
            ),
        ),
        migrations.CreateModel(
            name="Nonce",
            fields=[
                (
                    "id",
                    morango.models.fields.uuids.UUIDField(
                        editable=False, primary_key=True, serialize=False
                    ),
                ),
                ("timestamp", models.DateTimeField(default=django.utils.timezone.now)),
                ("ip", models.CharField(blank=True, max_length=100)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.AddField(
            model_name="certificate",
            name="salt",
            field=models.CharField(blank=True, max_length=32),
        ),
        migrations.AddField(
            model_name="syncsession",
            name="client_certificate",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="syncsessions_client",
                to="morango.certificate",
            ),
        ),
        migrations.AddField(
            model_name="syncsession",
            name="server_certificate",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="syncsessions_server",
                to="morango.certificate",
            ),
        ),
        migrations.CreateModel(
            name="InstanceIDModel",
            fields=[
                (
                    "id",
                    morango.models.fields.uuids.UUIDField(
                        editable=False, primary_key=True, serialize=False
                    ),
                ),
                ("platform", models.TextField()),
                ("hostname", models.TextField()),
                ("sysversion", models.TextField()),
                ("node_id", models.CharField(blank=True, max_length=20)),
                ("counter", models.IntegerField(default=0)),
                ("current", models.BooleanField(default=True)),
                ("db_path", models.CharField(max_length=1000)),
                (
                    "database",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="morango.databaseidmodel",
                    ),
                ),
                ("system_id", models.CharField(blank=True, max_length=100)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="SharedKey",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("public_key", morango.models.fields.crypto.PublicKeyField()),
                ("private_key", morango.models.fields.crypto.PrivateKeyField()),
                ("current", models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name="HardDeletedModels",
            fields=[
                (
                    "id",
                    morango.models.fields.uuids.UUIDField(
                        primary_key=True, serialize=False
                    ),
                ),
                ("profile", models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name="Buffer",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("serialized", models.TextField(blank=True)),
                ("deleted", models.BooleanField(default=False)),
                ("last_saved_instance", morango.models.fields.uuids.UUIDField()),
                ("last_saved_counter", models.IntegerField()),
                ("model_name", models.CharField(max_length=40)),
                ("profile", models.CharField(max_length=40)),
                ("partition", models.TextField()),
                ("model_uuid", morango.models.fields.uuids.UUIDField()),
                (
                    "transfer_session",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="morango.transfersession",
                    ),
                ),
                ("conflicting_serialized_data", models.TextField(blank=True)),
                ("_self_ref_fk", models.CharField(blank=True, max_length=32)),
                (
                    "source_id",
                    models.CharField(
                        max_length=96,
                    ),
                ),
                ("hard_deleted", models.BooleanField(default=False)),
            ],
            options={
                "abstract": False,
                "unique_together": {("transfer_session", "model_uuid")},
            },
        ),
        migrations.AddField(
            model_name="syncsession",
            name="extra_fields",
            field=models.TextField(default="{}"),
        ),
        migrations.AddField(
            model_name="syncsession",
            name="process_id",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddIndex(
            model_name="store",
            index=models.Index(
                fields=["partition"], name="idx_morango_store_partition"
            ),
        ),
        migrations.RenameField(
            model_name="syncsession",
            old_name="client_instance",
            new_name="client_instance_json",
        ),
        migrations.RenameField(
            model_name="syncsession",
            old_name="server_instance",
            new_name="server_instance_json",
        ),
        migrations.AddField(
            model_name="syncsession",
            name="client_instance_id",
            field=models.UUIDField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="syncsession",
            name="server_instance_id",
            field=models.UUIDField(blank=True, null=True),
        ),
    ]